#include <stdint.h>
#include <stdio.h>
#include "TPG.hh"
#include <stdlib.h>
#include <iostream>
using namespace std;
//NOTE11: Something that will come up a lot here is bit shifting with signed and unsigned integers
//and one big thing to note is that when assigning a narrower int to a wider int after a left bit shift
//you can lose information, as shown in this example from the 2019 Xilinx Vivado HLS user guide:
/*
ap_uint<13> Rslt;
ap_uint<7> Val1 = 0x41;
Rslt = Val1 << 6; // Yields: 0x0040, i.e. msb of Val1 is lost
Rslt = ap_uint<13>(Val1) << 6; // Yields: 0x1040, no info lost
ap_int<7> Val2 = -63;
Rslt = Val2 >> 4; //Yields: 0x1ffc, sign is maintained and extended
*/
//The results of the first two shows how you can lose bits from a left shift and how to avoid it.
//The result of the last one showcases the behavior of assigning a shifted signed ap_int to
//a wider unsigned ap_int, which is that it extends the 1's all the way to the wider's msb
//and *then* treats it as unsigned, so you can get quite a large number.
//There is a point in the following code where I can't tell if this behavior is anticipated,
//and I will note it
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
  //so if the if statement here is true for that it should also be true for (lincoeff & 0XFF0000) as is.
  //But maybe a shift is faster than reading through all those zeroes.
  //NOTE12: an interesting test might be changing this and seeing how the solution in Vivado changes.
  //RESULT: no change that i can see. commenting out bit shifted version as seems unnecessary
  //if (((lincoeff & 0XFF0000) >> 16) == 0) coeff = 0; //Linearization Coefficients 
  if ((lincoeff & 0XFF0000) == 0) coeff = 0; //Linearization Coefficients 
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
  // prod = correctedADC * mult;
  //Seems odd this if is after setting linearizerOutput. Waste of a step.
  //Might be optimized away?
  //NOTE13: Try changing this also.
  //So to figure out what's happening here, note that mult is an 8 bit number, so between
  //0 and 255. correctedADC is a 13 bit signed number, so between -4095 and 4095.
  //linearizerOutput is an 18 bit number, so between 0 and 262143.
  //If correctedADC is negative this is a bigg number, since linearizerOutput is unsigned the >>2 will extend
  //the ones but then those 1s will become just regular bits in an unsigned integer all the way at the
  //top. This behavior is immediately corrected though, so let's look at only the positive cases.
  //The min is obviously 0, and the max is 4095*255=1044225=11111110111100000001 which is 20 bits.
  //However, since it's bit shifted 2 to the right, we get 111111101111000000 which is 261056.
  //Note that this means for mult=1 the minimum correctedADC can be before hitting zero is b11=3
  //New info okay so the multiplication of two ap_ints will give back an ap_int that is
  //the width of the sum of their widths. In this case, cADC is 13 bits and mult is 8 bits, meaning it returns
  //a 21 bit signed number. However, this number is then shifted two towards zero (either left or right
  //if it is positive or negative), and because linearizerOutput is an unsigned 18 bit number, the most significant
  //three bits are cut off during its assignment. For a positive number this is basically like just removing
  //the two lsb and the msb.
  //linearizerOutput = (correctedADC * mult) >> 2; //Linearization Step Output
  //In this case, if cADC is negative, linearizerOutput becomes the shiftlin variable but shifted by 12 to the left.
  //From what I understand about bit shifting, this should lose the 12 msb of shiftlin, which, since it is 4 bits
  //total, is all of its information and it should become just 0.
  //NOTE14: don't know why this isn't just set to 0 if that's the case. Maybe set to zero.
  //RESULT: no change as far as i can tell, just setting to zero.
  //NOTE15: not sure why this isn't an if - else thing w/ lO above
  //if (correctedADC < 0) linearizerOutput = shiftlin << 12; 
  //RESULT: no change as far as i can tell, just changing to if else
  if (correctedADC < 0) linearizerOutput = 0; 
  else{
    linearizerOutput = (correctedADC * mult) >> 2; //Linearization Step Output
  }
  // Amplitude Filter
  // 4 Stage TAP
  //So we now set some m (18bit unsigned) equal to this number in the shift register
  //(18 bit unsigned). I had worried this might be undefined for the first loop,
  //but I think static variables are automatically initialized to zero so.
  m = r.shift_reg[3];
  //So this loop moves the everything in the 2-0 indices in r.shift_reg to the respective
  //3-1 indices.
  for (j = 3; j >= 1; j--){
//The UNROLL pragma essentially splits up the loop so that different iterations can be run in parallel.
#pragma HLS UNROLL
//The dependence pragma is essentially a way to tell HLS about variable dependence in the loop. Typically
//vivado will work this out for itself, but you can specificy variables to either remove or enforce dependence
//In this case, it's saying that the inter loop dependence for r.shift_reg is false.
//Which makes no sense to me, as it seems the order here is very important.
//But maybe if these are all run in parallel they are done at the same time kind of before
//being updated?
//NOTE16: Try commenting this out for testing
//RESULT: when commented out the latency min/max increased by 2, the interval min/max increased by 1, but
//the timing did not change. 4 less BRAMs were needed, 88 less DSP48Es were needed, 39789 more flip flops
//were needed, and 10126 less LUTs were needed. (note that this is with changes made previous so included the 24
//extra flip flops from before). Keeping as is for now
#pragma HLS dependence variable=r.shift_reg inter false
    r.shift_reg[j] = r.shift_reg[j-1];
  }
  //So then the new 0th indice is made by setting it to the linearizer Output.
  r.shift_reg[0] = linearizerOutput;
  //So this is the initial shift_reg[3] value being multiplied by the 4th indice in the weight array.
  //which is the -36. m is a positive number, so this will be some negative number.
  //And pro is a 25 bit signed number since 7+18=25.
  pro = m*weight[4];
  //pro is then bit shifted by shiftfilter which is set to 6
  //Because pro is signed, it will have its msb extended along the shift.
  //Not sure exactly why 6 but I figure it's just an acceptable amount of resolution loss on these values.
  mul = pro >> shiftfilter;
  //acc is a signed 19 bit number
  //Note that this has a small overflow problem because acc+mul returns a 20 bit number
  //but probably not a big deal. I think the overflow just cuts the msb off
  //NOTE17: ask prasanna about this
  acc = acc + mul;
  //Then it goes over the shift filter applying the weights, performing the shift, and adding up the results.
  //This is essentially checking the linearizerOutputs of each group of 5 incoming points
  //and adding them up with weights.
  for (j = 3; j >= 0; j--){
//The UNROLL pragma essentially splits up the loop so that different iterations can be run in parallel.
#pragma HLS UNROLL
    pro = r.shift_reg[j]*weight[j];
    mul = pro >> shiftfilter;
    acc = acc + mul;
  }
  //Not sure why this acc variable is necessary but I guess it's optimized out.
  filterOutput = acc;
  //If it's less than zero, then we give back 0. Also 0 if m == 0, so if the incoming shift_reg[3] was zero.
  //So this essentially puts us setting the sums all to zero for the first five values after the last <=0
  //result from linearizerOutput
  //Potential problem in that if it is possible to have a >0 filter output randomly
  //you could get that m!=0 before the first 0 you want to actually count from.
  //Potential fix by just checking if each previous value in the shiftreg is 0
  //unless we expected some bumpiness?
  //NOTE18: look into this
  if (filterOutput < 0 or m==0) filterOutput = 0;
  //If it's greater than this big amount it's set to that big amount.
  //I'm not even sure this should be possible since it's a 19 bit signed number
  //and above we already set it to zero if it's negative so that last bit shouldn't even be
  //in use theoretically.
  //NOTE19: try disabling in testing.
  //RESULT: no noticeable change. Commenting out.
  //Could also potentially make filterOutput a little smaller, since the returned peak is actually a max of
  //3FF, but maybe it's good to have this precision for the actual checking.
  //if (filterOutput > 0X3FFFF) filterOutput = 0X3FFFF;

  // Peak Finder
  //So now switching to the peak_reg of the register. First it checks if peak_reg is greater than the filterOutput (min 0)
  //then checks if it greater than the last peak_reg.
  if (r.peak_reg[0] > filterOutput && r.peak_reg[0] > r.peak_reg[1]){
    // Trigger Primitive Format 16 bits(6 bits timing information, 10 bits amplitude information) 
    //If it is, then we take in ampPeak and check if it's greater than some big number that is
    //significantly smaller than the big number filterOutput can be
    //and if it is we set it equal to that big number.
    //One thing I just realized is that peak_reg is a signed 19 bit variable but it should never be negative,
    //since it gets its values from filterOutput and that is set to zero if it's negative.
    //NOTE20: try changing peak_reg to an unsigned variable
    //RESULT: No timing change, required 6016 less flipflops and 4752 less LUTs. Keeping the change.
    //The reason it's set to this number specifically before bit shifting is that it will make that by-two bit shift
    //into 3FF, which is ten 1's. However, couldn't this be made slightly better with an if/else?
    //since if you just set ampPeak=3FF and do no bit shifting then you're good.
    /*
    if (r.peak_reg[0]> 0XFFF){
      tmpPeak = 0X03FF;
    }
    else{
      tmpPeak = r.peak_reg[0] >> 2;
    }
    */
   ampPeak = r.peak_reg[0];
   if (ampPeak > 0XFFF){
      ampPeak = 0XFFF;
    }
    //So then we shift it by two. Because ampPeak shouldn't be negative it follows that you shouldn't have
    //weird conversion issues w/ tempPeak. So you should never run that if
    //NOTE21: try removing the if in testing.
    //RESULT: No timing difference. Strangely enough seems to have reduced the LUT gain above from 4752 to 2288
    //rejecting change. Maybe look at again later
    tmpPeak = ampPeak >> 2;
    if (tmpPeak > 0X3FF){
      tmpPeak = 0X03FF;
    }
    
  }
  //Then the second index is set to the value of the first, and the first gets the new filterOutput value
  r.peak_reg[1] = r.peak_reg[0];
  r.peak_reg[0] = filterOutput;
  //tmpPeak is initialized to zero, so the function will return 0 until it finds a peak.
  return tmpPeak;
}
