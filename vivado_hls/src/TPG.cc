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
  //Note: is uint8_t ever defined?
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
  //The hex number here corresponds to 11111111111111 (14 bits).
  //This is saying that if the data_int is greater than 14 bits, there is an error.
  //data_int corresponds to link_in in the algo_unpacked function, which is set to only give
  //14 bits in.
  if (data_int > 0X3FFF) fprintf(stderr, "ERROR IN INPUT SAMPLE"); //Digi Input
  //The hex number here corresponds to 111111111111 (12 bits).
  //Ignores the first 8 bits since those are for the "link alignment markers", as mentioned in the N.B. in algo_unpacked.cpp
  uncorrectedADC = data_int & 0XFFF; //12 bits is the Digi information w/out weights.
  //The hex number here corresponds to 111111110000000000000000, so it selects that bit of lincoeff and then shifts
  //each bit 16 to the right. 
  //What seems odd to me is that this gets the bits *just* to the beginning and no further,
  //so if the if statement here is true for that it should also be true for lincoeff as is.
  //But maybe a shift is faster than reading through all those zeroes.
  //NOTE: an interesting test might be changing this and seeing how the solution in Vivado changes.
  if (((lincoeff & 0XFF0000) >> 16) == 0) coeff = 0; //Linearization Coefficients 
  else coeff = lincoeff;
  //So the base level is set by these coefficients, and this is what will be subtracted off the ADC.
  //The hex value here corresponds to 111111111111, so the first 12 bits is the pedestal.
  base = coeff & 0XFFF; //Pedestal
  //Hex value here corresponds to 1111000000000000, so the next 4 bits are the "Shift value"
  //From Prasanna presentation these are "the shift applied to the value obtained in the previous
  //step in order to obtain the linearizer output". The >> 12 of course moves these to the start.
  //Which is more efficient as shiftlin can then be a 4 bit number.
  shiftlin = (coeff & 0XF000) >> 12; //Shift Value
  //The hex here corresponds to 111111110000000000000000, so these are the remaining 8 bits of the 24 bit coeff,
  //and they correspond to the multiplication value that will <insert use here.>.
  //Again this is all shifted so that mult can be an 8 bit number.
  mult = (coeff & 0XFF0000) >> 16; //Multiplication value
  //As mentioned, this is just removing the base from the ADC to get the ADC we want to use.
  //This will be a 13 bit number because it takes into account the possibility of a negative result.
  correctedADC = (uncorrectedADC - base); // Subtract Pedestal
  //prod = correctedADC * mult;
  //Seems odd this if is after setting linearizerOutput. Waste of a step.
  //Might be optimized away?
  //NOTE: Try changing this also.
  //So to figure out what's happening here, note that mult is an 8 bit number, so between
  //0 and 255. correctedADC is a 13 bit signed number, so between -4095 and 4095.
  //linearizerOutput is an 18 bit number, so between 0 and 262143.
  //If correctedADC is negative this is nonsense, since
  //linearizerOutput is unsigned and >> shouldn't be used w/ negatives, so let's look at only the positive cases.
  //The min is obviously 0, and the max is 4095*255=1044225=11111110111100000001 which is 20 bits.
  //However, since it's bit shifted 2 to the right, we get 111111101111000000 which is 261056.
  //Note that this means for mult=1 the minimum correctedADC can be before hitting zero is b11=3
  linearizerOutput = (correctedADC * mult) >> 2; //Linearization Step Output
  //In this case, if cADC is negative, linearizerOutput becomes the shiftlin variable but shifted by 12 to the left.
  //shiftlin is a 4 bit number, so this gives us a range between 0 and 15. It's set to shift 12 to the left
  //which puts it as some set of numbers between 61440 and zero.
  //Don't understand why this is. <to be inputted>
  if (correctedADC < 0) linearizerOutput = shiftlin << 12; 

  // Amplitude Filter
  // 4 Stage TAP
  //So, and this is very confusing to me. We now set some m (18bit unsigned) equal to this number in the shift register
  //(18 bit unsigned).
  //However, as far as I can tell this number is not yet assigned.
  //Potentially maybe this is somehow getting the address instead? Not sure about this. <to be inputted>
  //NOTE: test this
  //NOTE: is it possible that the shift_reg retains its values over the looping?
  //this seems like it shouldn't be since it's initialized in algo_unpacked.
  m = r.shift_reg[3];
  //So this loop moves the everything in the 2-0 indices in r.shift_reg to the respective
  //3-1 indices. Not 100% sure why yet. <to be inputted>
  for (j = 3; j >= 1; j--){
//The UNROLL pragma <to be inputted>
#pragma HLS UNROLL
//The dependence pragma <to be inputted>
#pragma HLS dependence variable=r.shift_reg inter false
    r.shift_reg[j] = r.shift_reg[j-1];
  }
  //So then the new 0th indice is made by setting it to the linearizer Output.
  r.shift_reg[0] = linearizerOutput;
  //So this is the initial shift_reg[3] value being multiplied by the 4th indice in the weight array.
  //which is the -36. m is a positive number, so this will be some negative number.
  //And pro is a 25 bit signed number.
  pro = m*weight[4];
  //pro is then bit shifted by shiftfilter which is set to 6
  //which is doubly confusing as pro is negative since I don't think you're supposed to shift those.
  //but I guess potentially the shift could make it into a positive number somehow?
  mul = pro >> shiftfilter;
  //But acc is a signed 19 bit number, so clearly it's possible to be negative.
  acc = acc + mul;
  //Then it goes over the shift filter applying the weights, performing the shift, and adding up the results.
  //Now from what I recall this is essentially checking the adc of each group of 5 incoming points
  //and adding them up with weights.
  for (j = 3; j >= 0; j--){
//The UNROLL pragma <to be inputted>
#pragma HLS UNROLL
    pro = r.shift_reg[j]*weight[j];
    mul = pro >> shiftfilter;
    acc = acc + mul;
  }
  //Not sure why this variable is necessary but I guess it's optimized out.
  filterOutput = acc;
  //If it's less than zero, then we give back 0. Also 0 if m == 0, so if the incoming shift_reg[3] was zero.
  //<to be inputted>
  if (filterOutput < 0 or m==0) filterOutput = 0;
  //If it's greater than this big amount it's set to that big amount. <to be inputted>
  if (filterOutput > 0X3FFFF) filterOutput = 0X3FFFF;

  // Peak Finder
  //So now switching to the peak_reg of the register. First it checks if peak_reg is greater than the filterOutput (min 0)
  //then checks if it greater than the last peak_reg.
  if (r.peak_reg[0] > filterOutput && r.peak_reg[0] > r.peak_reg[1]){
    // Trigger Primitive Format 16 bits(6 bits timing information, 10 bits amplitude information) 
    //If it is, then we take in ampPeak and check if it's greater than some big number because <to be inputted>
    //and if it is we set it equal to that big number.
    ampPeak = r.peak_reg[0];
    if (ampPeak > 0XFFF){
      ampPeak = 0XFFF;
    }
    //Then we bit shift it to the right by 2
    //which is doubly confusing since it's able to be negative.
    //and then check if it's greater than some big value in which case we shift it
    //to a smaller number?
    //But also note that tmpPeak is unsigned so like this must be a negative positive conversion thing.
    tmpPeak = ampPeak >> 2;
    if (tmpPeak > 0X3FF){
      tmpPeak = 0X03FF;
    }
  }
  //Then the second index is set to the value of the first, and the first gets the new filterOutput value
  r.peak_reg[1] = r.peak_reg[0];
  r.peak_reg[0] = filterOutput;
  return tmpPeak;
}
