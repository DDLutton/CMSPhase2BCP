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

        static registers reg;
#pragma HLS ARRAY_PARTITION variable=reg complete dim=0

		ap_uint<2> j=link_in[0].range(3,0);
		ap_uint<192> output_word=0;

		uint24_t mycoeff = coeff[j];//0xb7506a;//coeff[lnk*NCrystalsPerLink+i]; // FIXME take the coefficient from LUTs

#pragma HLS UNROLL
		
		output_word.range(47, 32) = TPG(link_in[0].range(45, 32), mycoeff, reg);
		
		link_out[0]=output_word;

		for (int8_t lnk = 1; lnk < N_CH_IN; lnk++) {
#pragma HLS UNROLL
			link_out[lnk]=0;
	    }
	#ifndef __SYNTHESIS__
		cout << "shift " << reg.shift_reg[0] << " " << reg.shift_reg[1] << " " << reg.shift_reg[2] << " " << reg.shift_reg[3] << endl;
		cout << "peak " << reg.peak_reg[0] << " " << reg.peak_reg[1] << endl;
	#endif
	// Comment the following not to overwrite the output
	/*for (int8_t lnk = 0; lnk < N_CH_IN; lnk++) {
#pragma HLS UNROLL
//  pass-through "algo"
        link_out[lnk].range(7,0) = 0;
        link_out[lnk].range(191,8) = link_in[lnk].range(191,8) ;
    }*/
}

