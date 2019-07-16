#include <stdio.h>                                                                                                                                                                   
#include <stdlib.h>
#include <stdint.h>
#include <unistd.h>

#include <iostream>
#include <fstream>
#include <iomanip>
#include <string>

using namespace std;

//#include "algo_unpacked.h"   // This is where you should have had hls_algo - if not find the header file and fix this - please do not copy this file as that defines the interface
#include "../src/algo_unpacked.h"
#include "TPG.hh"
#include "../data/LUT.h"

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

void algo_unpacked(ap_uint<192> link_in[N_CH_IN], ap_uint<192> link_out[N_CH_OUT])
{

// !!! Retain these 4 #pragma directives below in your algo_unpacked implementation !!!
#pragma HLS ARRAY_PARTITION variable=link_in complete dim=0
#pragma HLS ARRAY_PARTITION variable=link_out complete dim=0
#pragma HLS PIPELINE II=3
#pragma HLS INTERFACE ap_ctrl_hs port=return

// null algo specific pragma: avoid fully combinatorial algo by specifying min latency
// otherwise algorithm clock input (ap_clk) gets optimized away
#pragma HLS latency min=3

        static registers reg[N_CH_IN][NCrystalsPerLink];
#pragma HLS ARRAY_PARTITION variable=reg complete dim=0
		static int j;
		ap_uint<192> output_word=0;
		ap_uint<192> debug_Out=0;
        ap_uint<192> linkIn_Out=0;
        debug_Out.range(47,32) = j;
		linkIn_Out = link_in[0];
		uint24_t mycoeff = coeff[j];//0xb7506a;//coeff[lnk*NCrystalsPerLink+i]; // FIXME take the coefficient from LUTs
		debug_Out.range(23,0) = mycoeff;
		for (int8_t i = 0; i < NCrystalsPerLink; i++){
#pragma HLS UNROLL
			short bitLo = (1+i)*16;
			short bitHi_in = bitLo+13; // digi inputs are 14 bits
			short bitHi_out = bitLo+15; // crystal outputs are 16 bits
			//If added so that the output_word's link_in section above isn't overwritten
			output_word.range(bitHi_out, bitLo) = TPG(link_in[0].range(bitHi_in, bitLo), mycoeff, reg[0][i]);
		}

		debug_Out.range(81,64) = reg[0][1].shift_reg[0];
		debug_Out.range(101,84) = reg[0][1].shift_reg[1];
		debug_Out.range(121,104) = reg[0][1].shift_reg[2];
		debug_Out.range(145,128) = reg[0][1].shift_reg[3];
		debug_Out.range(166,148) = reg[0][1].peak_reg[0];
		debug_Out.range(186,168) = reg[0][1].peak_reg[1];

		link_out[0]=output_word;
        link_out[1]=linkIn_Out;
		link_out[2]=debug_Out;

		for (int8_t lnk = 3; lnk < N_CH_IN; lnk++) {
#pragma HLS UNROLL
			link_out[lnk]=0;
	    }
	j+=1;
	#ifndef __SYNTHESIS__
		cout << "shift " << reg[0][1].shift_reg[0] << " " << reg[0][1].shift_reg[1] << " " << reg[0][1].shift_reg[2] << " " << reg[0][1].shift_reg[3] << endl;
		cout << "peak " << reg[0][1].peak_reg[0] << " " << reg[0][1].peak_reg[1] << endl;
	#endif
	// Comment the following not to overwrite the output
	/*for (int8_t lnk = 0; lnk < N_CH_IN; lnk++) {
#pragma HLS UNROLL
//  pass-through "algo"
        link_out[lnk].range(7,0) = 0;
        link_out[lnk].range(191,8) = link_in[lnk].range(191,8) ;
    }*/
}

