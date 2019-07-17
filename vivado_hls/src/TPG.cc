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

  uint18_t a = 0;
  uint18_t b = 0;
  uint18_t c = 0;
  uint18_t d=0;
  uint18_t e=0;


  int19_t mul = 0;
  int25_t pro = 0;
  int19_t acc = 0;
  int7_t weight[5] = {24, 31, 16, -35, -36}; //Filter Weights
  uint16_t tmpPeak = 0X0000;
  m = r.shift_reg[3];
  a=r.shift_reg[2];
  b=r.shift_reg[1];
  c=r.shift_reg[0];
  r.shift_reg[3] = a;
  r.shift_reg[2] = b;
  r.shift_reg[1] = c;
  d=r.peak_reg[1];
  e=r.peak_reg[0];
  r.peak_reg[1] = e;

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
    linearizerOutput = (correctedADC * mult) >> (shiftlin+2); //Linearization Step Output
  }

  r.shift_reg[0] = linearizerOutput;

  pro = m*weight[4];
  
  mul = pro >> shiftfilter;

  //NOTEB11: acc is a signed 19 bit number. This has a small potential for overflow since acc_mul returns a 20 bit number
  //Could try to changing acc to an array and then adding together the results to a int with enough bits to handle the
  //worst case scenario. Also, ask prasanna about this
  acc = acc + mul;
  pro = m*weight[3];
  mul = pro >> shiftfilter;
  acc = acc + mul;
  pro = a*weight[2];
  mul = pro >> shiftfilter;
  acc = acc + mul;
  pro = b*weight[1];
  mul = pro >> shiftfilter;
  acc = acc + mul;
  pro = c*weight[0];
  mul = pro >> shiftfilter;
  acc = acc + mul;

  filterOutput = acc;

  if (filterOutput < 0 or m==0) filterOutput = 0;
  r.peak_reg[0] = filterOutput;
  // Peak Finder
  if (e > filterOutput && e > d){
    // Trigger Primitive Format 16 bits(6 bits timing information, 10 bits amplitude information) 
    tmpPeak = e >> 2;
    if (tmpPeak > 0X3FF){
      tmpPeak = 0X03FF;
    }
    
  }
  return tmpPeak;
}
