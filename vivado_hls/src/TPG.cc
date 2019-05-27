#include <stdint.h>
#include <stdio.h>
#include "TPG.hh"
#include <stdlib.h>
#include <iostream>
using namespace std;

uint16_t TPG(uint14_t data_int, uint24_t lincoeff, registers &r){
  int8_t j;
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
  int19_t ampPeak = 0;
  uint16_t tmpPeak = 0X0000;

  // Linearizer
  if (data_int > 0X3FFF) fprintf(stderr, "ERROR IN INPUT SAMPLE"); //Digi Input
  uncorrectedADC = data_int & 0XFFF; //12 bits is the Digi information, last 2 bits is gain information
  if (((lincoeff & 0XFF0000) >> 16) == 0) coeff = 0; //Linearization Coefficients 
  else coeff = lincoeff;
  base = coeff & 0XFFF; //Pedestal
  shiftlin = (coeff & 0XF000) >> 12; //Shift Value
  mult = (coeff & 0XFF0000) >> 16; //Multiplication value
  correctedADC = (uncorrectedADC - base); // Subtract Pedestal
  //prod = correctedADC * mult;
  linearizerOutput = (correctedADC * mult) >> (shiftlin + 2); //Linearization Step Output
  if (correctedADC < 0) linearizerOutput = shiftlin << 12; 

  // Amplitude Filter
  // 4 Stage TAP
  m = r.shift_reg[3];
  for (j = 3; j >= 1; j--){
#pragma HLS UNROLL
#pragma HLS dependence variable=r.shift_reg inter false
    r.shift_reg[j] = r.shift_reg[j-1];
  }
  r.shift_reg[0] = linearizerOutput;
  pro = m*weight[4];
  mul = pro >> shiftfilter;
  acc = acc + mul;
  for (j = 3; j >= 0; j--){
#pragma HLS UNROLL
    pro = r.shift_reg[j]*weight[j];
    mul = pro >> shiftfilter;
    acc = acc + mul;
  }
  filterOutput = acc;
  if (filterOutput < 0 or m==0) filterOutput = 0;
  if (filterOutput > 0X3FFFF) filterOutput = 0X3FFFF;

  // Peak Finder
  if (r.peak_reg[0] > filterOutput && r.peak_reg[0] > r.peak_reg[1]){
    // Trigger Primitive Format 16 bits(6 bits timing information, 10 bits amplitude information) 
    ampPeak = r.peak_reg[0];
    if (ampPeak > 0XFFF){
      ampPeak = 0XFFF;
    }
    tmpPeak = ampPeak >> 2;
    if (tmpPeak > 0X3FF){
      tmpPeak = 0X03FF;
    }
  }
  r.peak_reg[1] = r.peak_reg[0];
  r.peak_reg[0] = filterOutput;
  return tmpPeak;
}
