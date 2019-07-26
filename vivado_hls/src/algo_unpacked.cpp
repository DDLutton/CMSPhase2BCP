#include <stdio.h>                                                                                                                                                                   
#include <stdlib.h>
#include <stdint.h>
#include <unistd.h>

#include <iostream>
#include <fstream>
#include <iomanip>
#include <string>

//Since this is shared code, as a note the comments starting like //[comment] rather than // [comment ] are the ones I am making
//whereas the latter are mostly from the commenting on the original files from the APx_Gen0_Algo repository (the main exception being the TPG files).

using namespace std;
//Note: I don't want to remove it right now since I haven't actually tested with it, but there's no reason I can see that
//it shouldn't just be #include "algo_unpacked.h"
//#include "algo_unpacked.h"   // This is where you should have had hls_algo - if not find the header file and fix this - please do not copy this file as that defines the interface
#include "../src/algo_unpacked.h"
#include "TPG.hh"
#include "../data/LUT.h"

const int NCrystalsPerLink = 11; // Bits 16-31, 32-47, ..., 176-191, keeping range(15, 0) unused
//Defines how many links and crystals you want the TPG to run over
//28 Links and 11 crystals gets you 308 inputs, which is just over the total amount of crystals we'll need.
const int NLinksEval = 28;
const int NCrystalsEval = 11;
 /*
  * algo_unpacked interface exposes fully unpacked input and output link data.
  * This version assumes use of 10G 8b10b links, and thus providing 192bits/BX/link.
  *
  * !!! N.B.: Do NOT use the first bytes of link_in/link_out (i.e. link_in/link_out[].range(7,0)
  * as this portion is reserved for transmission of 8b10b input/output link alignment markers.
  *
  * The remaining 184 bits are available for algorithm use.
  *
  * !!! N.B. 2: make sure to assign every bit of link_out[] data. First byte should be assigned zero.
  */

//ToChange: The way the APx framework works seems to be with 48 links by default. We don't need this many
//could potentially figure out if it's possible to alter the framework, or additionally changing how the link_in stores data
//so that there are only 7 crystals per link would get closest to 300 crystals (though 300/48 isn't an integer so there's
//no way to get exactly 300 without dropping some links)
//For now just letting the excess links pass through seems to work.
void algo_unpacked(ap_uint<192> link_in[N_CH_IN], ap_uint<192> link_out[N_CH_OUT])
{

//Partitioning the coeff array from LUT.h. Since the array is set up as a 2D array for each
//crystal with 3 gain values, I've partitioned dim=1 which is the crystals
//However I have seen some messages during the rtl creation that indicate to me that, due to
//the small size of the second dimension it's automatically partitioning those as well.
//So this may be equivalent to just complete dim=0 (which partitions everything)
#pragma HLS ARRAY_PARTITION variable=coeff complete dim=1
// !!! Retain these 4 #pragma directives below in your algo_unpacked implementation !!!
#pragma HLS ARRAY_PARTITION variable=link_in complete dim=0
#pragma HLS ARRAY_PARTITION variable=link_out complete dim=0
#pragma HLS PIPELINE II=3
#pragma HLS INTERFACE ap_ctrl_hs port=return

// null algo specific pragma: avoid fully combinatorial algo by specifying min latency
// otherwise algorithm clock input (ap_clk) gets optimized away
//Since it's a latency min, this probably doesn't need to be here for most algorithms of a sufficient level of complexity, but
//it might reduce rtl creation time by limiting the search space.
#pragma HLS latency min=3

		//Having this as static but without a reset pragma applied in HLS gives a lot of warnings,
		//but as far as I can tell doesn't seem to mess with the hardware output: the registers (and static variables in general)
		//are automatically initialized to zero during configuration it seems
		//ToChange: Would still be good to try adding the reset pragma to make sure 
		//and is potentially necessary for later functionality
        static registers reg[NLinksEval][NCrystalsEval];
#pragma HLS ARRAY_PARTITION variable=reg complete dim=0

		//Using NLinksEval instead of N_CH_IN to 
		//ToChange: For some reason there seems to be differences in using the UNROLL pragma vs manually loop unrolling
		//so it might be interesting to unroll these loops manually, which, though long, should be straightforward to generate the code for.
		for (int8_t lnk = 0; lnk < NLinksEval; lnk++) {
#pragma HLS UNROLL

			ap_uint<192> output_word=0;

			for (int8_t i = 0; i < NCrystalsEval; i++){
#pragma HLS UNROLL

				short bitLo = (1+i)*16;
				short bitHi_in = bitLo+13; // digi inputs are 14 bits
				short bitHi_out = bitLo+15; // crystal outputs are 16 bits

				//j here reads in the gain from link_in which can be used to
				//select the coefficients with the new way they are stored.
				//As a note, since the majority of the crystals are set to 0000, which as I understand it is not
				//an actual value they'd give back, I added 1's to the gain for each 0000 crystal that is run over so that it's still
				//selecting a valid coefficient.
				//The code for generating input files like this is included in the python directory
				ap_uint<2> j=link_in[lnk].range(bitHi_in,bitHi_in-1);
				
				uint24_t mycoeff = coeff[(lnk*NCrystalsEval)+i][j-1]; // FIXME take the coefficient from LUTs
				output_word.range(bitHi_out, bitLo) = TPG(link_in[lnk].range(bitHi_in, bitLo), mycoeff, reg[lnk][i]);
			}
			link_out[lnk]=output_word;
		}


	//For the simulations this will list out every reg value for each crystal that actually receives data input
	//There are times (not uncommon) when the csim might pass due to finding the peak in the correct location and
	//with enough intensity to read out 03ff, but with some small mistake that leads to the shift registers being incorrect
	//So I've included a set of files that represent the correct output here and you can check the output against them.
	#ifndef __SYNTHESIS__
		static int countr = 0;
		cout << "start " << countr << endl;
		for (int l = 0; l < NLinksEval; l++){
			cout << "shift " << l << " " <<  reg[l][1].shift_reg[0] << " " << reg[l][1].shift_reg[1] << " " << reg[l][1].shift_reg[2] << " " << reg[l][1].shift_reg[3] << endl;
			cout << "peak " << l << " "<< reg[l][1].peak_reg[0] << " " << reg[l][1].peak_reg[1] << endl;
			cout << "next" << endl;
		}
		countr +=1;
	#endif
	// Comment the following not to overwrite the output
	//I uncommented this to run over all the links that we don't take data from.
	//This is potentially unnecessary, but is probably insignificant in terms of total resources and
	//there's no reason I can think of that this should increase latency.
	//So I keep it in as vivado spits out a lot of warnings if you have inputs that don't
	//go anywhere.
	for (int8_t lnk = NLinksEval; lnk < N_CH_IN; lnk++) {
#pragma HLS UNROLL
//  pass-through "algo"
        	link_out[lnk].range(7,0) = 0;
        	link_out[lnk].range(191, 8) = link_in[lnk].range(191, 8) ;
	}
}

