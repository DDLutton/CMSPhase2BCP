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
#include "../../../../../APx_Gen0_Algo/VivadoHls/null_algo_unpacked/vivado_hls/src/algo_unpacked.h"
#include "TPG.hh"

const uint4_t NCrystalsPerLink = 11; // Bits 16-31, 32-47, ..., 176-191, keeping range(15, 0) unused

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

        for (int lnk = 0; lnk < N_CH_IN; lnk++) {
#pragma HLS UNROLL

           static registers reg[NCrystalsPerLink];
//#pragma HLS PIPELINE II=5
#pragma HLS ARRAY_PARTITION variable=reg complete dim=0

           short i;
           for (i = 0; i < NCrystalsPerLink; i++){
#pragma HLS UNROLL
               int bitLo=(1+i)*16;
	       int bitHi_in=bitLo+13; // digi inputs are 14 bits
               int bitHi_out=bitLo+15; // crystal outputs are 16 bits
	       uint24_t mycoeff=0xb7506a; // FIXME take the coefficient from LUTs
               link_out[lnk].range(bitHi_out,bitLo)=TPG(link_in[lnk].range(bitHi_in,bitLo), mycoeff, reg[i], i);
           }
  	}

	// Comment the following not to overwrite the output
	for (int lnk = 0; lnk < N_CH_IN; lnk++) {
#pragma HLS UNROLL
//  pass-through "algo"
        link_out[lnk].range(7,0) = 0;
        link_out[lnk].range(191,8) = link_in[lnk].range(191,8) ;
    }
}
