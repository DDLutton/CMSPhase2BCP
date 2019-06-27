#include <stdint.h>
#include <stdio.h>
#include "TPG.hh"
#include <stdlib.h>
#include <iostream>
using namespace std;
uint16_t TPG(uint14_t data_int, uint24_t lincoeff, registers &r){
  int13_t correctedADC = 0;
  uint12_t uncorrectedADC = 0;
  uint18_t linearizerOutput = 0;
  uint12_t base = 0;
  uint24_t coeff = 0;
  uint4_t shiftlin = 0;
  uint8_t mult = 0;
  int21_t prod = 0;
  int19_t filterOutput = 0;
  uint4_t shiftfilter = 6;
  uint18_t m = 0;
  int19_t mul = 0;
  int25_t pro = 0;
  int19_t acc = 0;
  int7_t weight[5] = {24, 31, 16, -35, -36}; //Filter Weights
  uint16_t tmpPeak = 0X0000;

  // Linearizer

  if (data_int > 0X3FFF) fprintf(stderr, "ERROR IN INPUT SAMPLE"); //Digi Input

  uncorrectedADC = data_int & 0XFFF; //12 bits is the Digi information w/out weights.
  if ((lincoeff & 0XFF0000) == 0) coeff = 0; //Linearization Coefficients 
  else coeff = lincoeff;

  base = coeff & 0XFFF; //Pedestal
  
  shiftlin = (coeff & 0XF000) >> 12; //Shift Value
  
  mult = (coeff & 0XFF0000) >> 16; //Multiplication value
  
  correctedADC = (uncorrectedADC - base); // Subtract Pedestal
  // prod = correctedADC * mult;

  if (correctedADC < 0) linearizerOutput = 0; 
  else{
    linearizerOutput = (correctedADC * mult) >> 2; //Linearization Step Output
  }
  // Amplitude Filter
  // 4 Stage TAP
  
  //NOTEB9: Static variables should be initialized to 0. Is this the case post-synthesis?
  m = r.shift_reg[3];
  //So this loop moves the everything in the 2-0 indices in r.shift_reg to the respective
  //3-1 indices.
  for (int3_t j = 3; j >= 1; j--){
#pragma HLS UNROLL
//The dependence pragma is essentially a way to tell HLS about variable dependence in the loop. Typically
//vivado will work this out for itself, but you can specificy variables to either remove or enforce dependence
//NOTEB10: The dependence here seems true to me. Ask Prasanna about it.
#pragma HLS dependence variable=r.shift_reg inter false
    r.shift_reg[j] = r.shift_reg[j-1];
  }

  r.shift_reg[0] = linearizerOutput;

  pro = m*weight[4];
  
  mul = pro >> shiftfilter;

  //NOTEB11: acc is a signed 19 bit number. This has a small potential for overflow since acc_mul returns a 20 bit number
  //Could try to changing acc to an array and then adding together the results to a int with enough bits to handle the
  //worst case scenario. Also, ask prasanna about this
  acc = acc + mul;

  for (int8_t j = 3; j >= 0; j--){
#pragma HLS UNROLL
    pro = r.shift_reg[j]*weight[j];
    mul = pro >> shiftfilter;
    acc = acc + mul;
  }

  filterOutput = acc;

  //NOTEB12: Potential problem if we get a non-zero m randomly before the actual grouping we want.
  //But maybe am misunderstanding. Ask Prasanna.
  if (filterOutput < 0 or m==0) filterOutput = 0;

  // Peak Finder
  if (r.peak_reg[0] > filterOutput && r.peak_reg[0] > r.peak_reg[1]){
    // Trigger Primitive Format 16 bits(6 bits timing information, 10 bits amplitude information) 
    tmpPeak = r.peak_reg[0] >> 2;
    if (tmpPeak > 0X3FF){
      tmpPeak = 0X03FF;
    }
    
  }
  r.peak_reg[1] = r.peak_reg[0];
  r.peak_reg[0] = filterOutput;
  return tmpPeak;
}
