#include <stdio.h>                                                                                                                                                                   
#include <stdlib.h>
#include <stdint.h>
#include <unistd.h>

#include <iostream>
#include <fstream>
#include <iomanip>
#include <string>

using namespace std;
//Not entirely sure what is happening here. In the current git commit the algo_unpacked.h file is in the same folder
//as the TPG.hh file which is in the same folder as the algo_unpacked stuff (all in src)
//What is hls_algo?
//#include "algo_unpacked.h"   // This is where you should have had hls_algo - if not find the header file and fix this - please do not copy this file as that defines the interface
#include "../src/algo_unpacked.h"
#include "TPG.hh"
#include "../data/LUT.h"

const int NCrystalsPerLink = 11; // Bits 16-31, 32-47, ..., 176-191, keeping range(15, 0) unused
//Note: N.B. means "note well" or something in Latin, so, you know, "note well".
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

void algo_unpacked(ap_uint<192> link_in[N_CH_IN], ap_uint<192> link_out[N_CH_OUT], int j)
{

// !!! Retain these 4 #pragma directives below in your algo_unpacked implementation !!!
//Note that in the debug mode in vivado for the C simulation, you have a bunch of variables being "optimized out" which can make
//it harder to follow along. I'm not sure, but I suspect disabling these pragma lines would make it more clear.
//Obviously they would need to be reenabled at synthesis time since they are the optimizations.
//ARRAY_PARTITION basically takes regular arrays and turns them into just
//a bunch of individual variables of the type that the array is holding.
//This is doing it to the link_in and link_out variables, which are essentially the arrays that hold the input
//and output data
#pragma HLS ARRAY_PARTITION variable=link_in complete dim=0
#pragma HLS ARRAY_PARTITION variable=link_out complete dim=0
//Pipeline basically allows the system to process new input while other input is being worked on
//instead of waiting for the last input to finish. This reduces the number of clock cycles it takes for
//some amount of input to be processed.
//The 3 here means that it can process new input every 3 clock cycles. I'm not sure exactly why this is the case
//instead of 1, but I guess it could either be concerns about using up too many resources
//on the FPGA, or potentially there is a bottleneck that makes going below 3 unhelpful,
//though I'm not sure exactly what form that would take.
#pragma HLS PIPELINE II=3
//INTERFACE seems kinda complicated, and essentially has to do with the input and output protocols of functions.
//In this case, ap_ctrl_hs means that a set of "control ports" that tell the function to "start", and say when it's "idle",
//"done", and "ready" for new data.
//The "port" specifies which part of the function this pragma applies to. In this case it applies to the, I assume,
//returning of the output data. I'm a little confused by the fact that this function doesn't return anything.
//But rather seems to work by changing the link_out array which doesn't require a return.
//However, I see this being used elsewhere with void functions so I really don't know now.
#pragma HLS INTERFACE ap_ctrl_hs port=return
   
// null algo specific pragma: avoid fully combinatorial algo by specifying min latency
// otherwise algorithm clock input (ap_clk) gets optimized away
//So setting a latency min is pretty much what it sounds like. For this algo_unpacked function the minimum
//number of clock cycles it is allowed to take is 3. The reason is given above, but I'm not sure exactly
//why it's a bad thing for that bit to get optimized away. Maybe it makes the thing not work?
//Additionally, I read that this can be used to speed up how fast the synthesis goes for a given solution,
//since it can ignore possibilities with latency above/below the max/min.
#pragma HLS latency min=3
	//The "registers" is a struct defined in TPG.hh which is composed of an array (size 4) of 18 bit unsigned ints
	//and an array (size 2) of 19 bit signed ints
	//so each element of the array can have two signed ints and 4 unsigned ints.
	//Here we have a big 2D array of registers, whose size is dependent on the number of channels
	//and the number of crystals
    static registers reg[N_CH_IN][NCrystalsPerLink];
//Array partition stuff same as before.
#pragma HLS ARRAY_PARTITION variable=reg complete dim=0
	//Looping over each link in the incoming data. Here it is 48 links.
	for (int8_t lnk = 0; lnk < N_CH_IN; lnk++) {
//The UNROLL pragma <to be inputted>
#pragma HLS UNROLL
		ap_uint<192> output_word;
		//Then looping over each crystal contained in the link.
		for (int8_t i = 0; i < NCrystalsPerLink; i++){
//The UNROLL pragma <to be inputted>
#pragma HLS UNROLL
			//Getting the bit positions and range of specifically the crystal inputs, *not* the metadata from the links
			//bitLo is moved forward 16 bits (4 hex) because the first 16 bits is metadata
			//Then the rest of the digi input is 14 bits 
			//NOTE: I still don't fully understand what happens w/ the last 2 bits.
			//NOTE: Not sure why these are specifically shorts. They go up to,at most (NCrystalsPerLink*16)+15
			//which at current is like 8 bits so I dunno.
			short bitLo = (1+i)*16;
			short bitHi_in = bitLo+13; // digi inputs are 14 bits
			short bitHi_out = bitLo+15; // crystal outputs are 16 bits
			//The coeff array is defined in LUT.h, and essentially contains the 8 bit base level response (pedestal);
			//the 4 bit shift value; and the 8 bit
			uint24_t mycoeff = coeff[lnk*10+j];//0xb7506a;//coeff[lnk*NCrystalsPerLink+i]; // FIXME take the coefficient from LUTs
			//cout << "Input " << link_in[lnk].range(bitHi_in, bitLo) << " " << mycoeff << endl;
			//Note, the .range() method on ap_int operators specifically deals with bits.
			//This is the actual linearization, FIL, and Peakfinder bit
			output_word.range(bitHi_out, bitLo) = TPG(link_in[lnk].range(bitHi_in, bitLo), mycoeff, reg[lnk][i]);
		}
		//After filling up output_word w/ the results of TPG, we throw it to link_out.
		//Probably optimized in the system anyway, but why not just have link_out in the place of output_word
		link_out[lnk]=output_word;
	}
	//Seems to be just a test, giving out the first shift values and the first peak values in the reg.
	cout << "shift " << reg[0][1].shift_reg[0] << " " << reg[0][1].shift_reg[1] << " " << reg[0][1].shift_reg[2] << " " << reg[0][1].shift_reg[3] << endl;
	cout << "peak " << reg[0][1].peak_reg[0] << " " << reg[0][1].peak_reg[1] << endl;

	// Comment the following not to overwrite the output
	/*for (int8_t lnk = 0; lnk < N_CH_IN; lnk++) {
#pragma HLS UNROLL
//  pass-through "algo"
        link_out[lnk].range(7,0) = 0;
        link_out[lnk].range(191,8) = link_in[lnk].range(191,8) ;
    }*/
}

