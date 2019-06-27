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
#include "algo_unpacked.h"   // This is where you should have had hls_algo - if not find the header file and fix this - please do not copy this file as that defines the interface
//#include "../src/algo_unpacked.h"
#include "TPG.hh"
#include "../data/LUT.h"
//NOTEB3: this may or may not be true. From what I gathered from speaking to Prasanna, it seems like
//the 48-63 range is what we want to avoid.
const int NCrystalsPerLink = 11; // Bits 16-31, 32-47, ..., 176-191, keeping range(15, 0) unused
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
//ARRAY_PARTITION basically takes regular arrays and turns them into just
//a bunch of individual variables of the type that the array is holding.
#pragma HLS ARRAY_PARTITION variable=link_in complete dim=0
#pragma HLS ARRAY_PARTITION variable=link_out complete dim=0
//Pipeline basically allows the system to process new input while other input is being worked on
//instead of waiting for the last input to finish.
//The 3 here means that it can process new input every 3 clock cycles. I'm not sure exactly why this is the case
//instead of 1.
//NOTEB4: Try with 1 or ask Prasanna why 1.
#pragma HLS PIPELINE II=3
//INTERFACE seems kinda complicated, and essentially has to do with the input and output protocols of functions.
//In this case, ap_ctrl_hs means that a set of "control ports" that tell the function to "start", and say when it's "idle",
//"done", and "ready" for new data.
//NOTEB5: Figure out the meaning of "return"
#pragma HLS INTERFACE ap_ctrl_hs port=return
   
// null algo specific pragma: avoid fully combinatorial algo by specifying min latency
// otherwise algorithm clock input (ap_clk) gets optimized away
//So setting a latency min is pretty much what it sounds like. For this algo_unpacked function the minimum
//number of clock cycles it is allowed to take is 3. The reason is given above, but I'm not sure exactly what it means.
//NOTEB6: Try disabling or ask Prasanna why 3.
#pragma HLS latency min=3

	//Very important to note that this is specifically a "static" variable. This means if you, for instance
	//call algo_unpacked twice, it will keep the values it had in it from last time.
    static registers reg[N_CH_IN][NCrystalsPerLink];
#pragma HLS ARRAY_PARTITION variable=reg complete dim=0

	for (uint8_t lnk = 0; lnk < N_CH_IN; lnk++) {
//The UNROLL pragma essentially splits up the loop so that different iterations can be run in parallel.
#pragma HLS UNROLL
		ap_uint<192> output_word;
		//NOTEB7: I've changed this to avoid bits 48-63 instead of 0-15. Figure out if this is correct from Prasanna.
		output_word.range(63,48)=link_in[lnk].range(63,48);
		for (uint8_t i = 0; i <= NCrystalsPerLink; i++){
#pragma HLS UNROLL
			if (i==3){
				continue;
			}
			short bitLo = i*16;
			short bitHi_in = bitLo+13; // digi inputs are 14 bits
			short bitHi_out = bitLo+15; // crystal outputs are 16 bits
			uint24_t mycoeff = coeff[lnk*10+j];//0xb7506a;//coeff[lnk*NCrystalsPerLink+i]; // FIXME take the coefficient from LUTs
			//cout << "Input " << link_in[lnk].range(bitHi_in, bitLo) << " " << mycoeff << endl;
			if (i>3){
				output_word.range(bitHi_out, bitLo) = TPG(link_in[lnk].range(bitHi_in, bitLo), mycoeff, reg[lnk][i-1]);
			}
			else {
				output_word.range(bitHi_out, bitLo) = TPG(link_in[lnk].range(bitHi_in, bitLo), mycoeff, reg[lnk][i]);
			}
		} 
		//NOTEB8: Why not just set link_out above insetad of this middleword stuff?
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

