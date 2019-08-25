#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 10:42:44 2019

@author: dylanlutton
"""


#This program is to take in the input from the 100Events_300Channels file
#and use the TPG to determine how the registers need to be initialized such that we don't have a filter problem

import re
import numpy as np

from WritingOutputRef_VariableLinks import registers 


def ADCtoLin(data_int,lincoeff):
  uncorrectedADC = data_int & 0XFFF
  if (((lincoeff & 0XFF0000) >> 16) == 0): coeff = 0
  else: coeff = lincoeff
  base = coeff & 0XFFF
  shiftlin = (coeff & 0XF000) >> 12
  mult = (coeff & 0XFF0000) >> 16 
  correctedADC = (uncorrectedADC - base)
  prod = correctedADC * mult 
  linearizerOutput = prod >> (shiftlin + 2)
  if (linearizerOutput > 0X30000 or correctedADC < 0): linearizerOutput = 0
  return linearizerOutput
  
def LintoADC(lin,lincoeff):
  tooFarDown = False
  tooFarUp = False
  
  if (((lincoeff & 0XFF0000) >> 16) == 0): coeff = 0
  else: coeff = lincoeff
  base = coeff & 0XFFF
  shiftlin = (coeff & 0XF000) >> 12
  mult = (coeff & 0XFF0000) >> 16 
  
  prod = int(lin) << (shiftlin+2)
  correctedADC = prod // mult
  uncorrectedADC = correctedADC + base
  
  #Test to make sure it works
  testlin = ADCtoLin(uncorrectedADC,lincoeff)
  while (testlin != lin):
      if tooFarDown and tooFarUp:
          print("weeoooweeoooo, breakdown of the system alert!")
          print(lin,testlin,uncorrectedADC,lincoeff)
          break
      if testlin > lin:
          tooFarUp = True
          uncorrectedADC -= 1
          testlin = ADCtoLin(uncorrectedADC,lincoeff)
      elif testlin < lin:
          tooFarDown = True
          uncorrectedADC += 1
          testlin = ADCtoLin(uncorrectedADC,lincoeff)
  return uncorrectedADC


filename = "100Events_300Channels"

#Creates a fake init event for each event
initAllEvents = True

if initAllEvents:
    #Number of events to initialize
    NEvents = 100
    sol = np.zeros((NEvents,300,4),dtype = int)
    coeffAr = np.zeros((NEvents,300,4),dtype = int)

else:
      sol = np.zeros((300,4))
      coeffAr = []



weights = np.array([24,31,16,-35,-36])
out = False
linearAr = []
peakAr = []

outIter = 0
skip = 0
cryCount = 0
evtCtr = 0
with open(filename) as inFile:
    reg = registers()
    lstReg = registers()
    for k,line in enumerate(inFile):
        #Skips however many lines are put into skip
        if skip > 0:
            skip = skip - 1
            continue
        #Gets the event number
        if "Treating event" in line:
            evtCtr =  int(re.split(r'[ \n]', line)[5][:-1])
            cryCount = 0
            if not initAllEvents:
                if evtCtr >1:
                    break
            elif evtCtr > NEvents:
                break
            continue
            
        
        elif "*** Channel ***" in line:
            #Resetting out and adcCount

            out = False
            outIter = 0
            adcCount = 0
            linearAr = []
            peakAr = []
            reg = registers()
            skip = 1
            continue
        
        elif "output" in line:
            out = True
            continue
        
        lineAr = re.split(r'[ \n]', line)
        
        if out:
            if outIter == 0:
                #Getting the first four linOuts from the data
                for i in range(4):
                    linearAr.append(int(lineAr[i]))
                    #Adding the first linout twice to the last bits of the shift_reg, and then adding next two
                    #shift_reg[3], being the same as shift_reg[2], is just a placeholder for the variable we want to solve for
                    if i<2:
                        reg.shift_reg[3-i] = linearAr[0]
                    elif i<4:
                        reg.shift_reg[3-i] = linearAr[i-1]

                    
                outIter +=1
                skip = 1
                continue
            elif outIter == 1:
                peakAr.append(0)
                
                #Getting first three outputs from the filter output in data
                #Only first three because the filter output is shifted one up from the linearizer output, so we don't actually know the filter output
                #corresponding to the adc input that go the first linearizerOutput
                #In this case it's assumed to be zero
                for i in range(3):
                    peakAr.append(int(lineAr[i]))
                    #Getting the 2nd and 3rd filter output. Again because the data is shifted, these will
                    #correspond to the 3rd and 4th linearizer outputs.
                    if i >= 1 and i < 3:
                        reg.peak_reg[2-i] = peakAr[i]
                
                for el in peakAr:
                    if (el != 0):
                        print("oooonoooo")
                #Solving for the unknown linOuts based on the filter outputs for
                #first the 4th adc input (having only one unknown)
                #and then the 3rd, etc
                acc = 0
                for j in range(4):
                    acc = 0
                    acc = (linearAr[3-j]*weights[0]) >> 6
                    for i in range(3):
                        acc += (weights[i+1]*reg.shift_reg[i]) >> 6
                    #If the filter output we're solving for is zero, first a check is done that just copying the next linOut
                    #for the unknown works to become less than zero (as linOuts, if negative, are moved to zero)
                    #and if not then finding the linOut that gets it to be exactly zero
                    if peakAr[3-j] == 0:
                        accTest = acc + ((weights[4]*reg.shift_reg[3]) >> 6)
                        if accTest <= 0:
                            if initAllEvents:
                                sol[evtCtr-1,cryCount,3-j] = reg.shift_reg[3]
                            else:
                                sol[cryCount,3-j] = reg.shift_reg[3]
                        else:
                            reg.shift_reg[3] = ((-acc) << 6) // (weights[4])
                            if initAllEvents:
                                sol[evtCtr-1,cryCount,3-j] = reg.shift_reg[3]
                            else:
                                sol[cryCount,3-j] = reg.shift_reg[3]
                    elif peakAr[3-j] < 0:
                        print("WEEEOOOWEEEOO ERROR IN DATA AAAAAAAAAAAAAAAAAAAAAAAAAAA")
                        raise ValueError("Hey why is your filter output under zero??")
                    else:
                        reg.shift_reg[3] = ((peakAr[3-j]-acc) << 6) // (weights[3])
                        if initAllEvents:
                            sol[evtCtr-1,cryCount,3-j] = reg.shift_reg[3]
                        else:
                            sol[cryCount,3-j] = reg.shift_reg[3]
                    #Shifting all the registers one back, but leaving the last register as the
                    #solution just found
                    reg.shift_reg[0] = reg.shift_reg[1]
                    reg.shift_reg[1] = reg.shift_reg[2]
                    reg.shift_reg[2] = reg.shift_reg[3]

                cryCount += 1
                skip = 4
                continue
        else:
            if adcCount >=4:
                continue
            #Getting the gain
            gainVal = int(lineAr[0])
            #Getting the component parts of the coefficients
            coPed = hex(int(lineAr[2]))[2:].zfill(3)
            coShift = hex(int(lineAr[3]))[2:].zfill(1)
            coMult = hex(int(lineAr[4]))[2:].zfill(2)
            #Putting the coefficient together
            if initAllEvents:
                coeffAr[evtCtr-1,cryCount,adcCount] = int("0x{0}{1}{2}".format(coMult,coShift,coPed),16)
            else:
                coeffAr.append(int("0x{0}{1}{2}".format(coMult,coShift,coPed),16))
            adcCount +=1

#Getting the adcInp from the determined linOuts
#If the adc from a converted linOut fails to reconvert back into the same linOut
#then the ADC is moved upwards or downwards appropriately until it does
if initAllEvents:
    #uniqueCoeffAr = np.array([np.array([coSet[i] for i in range(0,1200,4)],dtype = int) for coSet in coeffAr])
    adcInp = np.zeros((NEvents,300,10),dtype = int)
    for i,evtZip in enumerate(zip(coeffAr,sol)):
        for j in range(300):
            for k in range(4):
                adcInp[i,j,6+k] = LintoADC(evtZip[1][j][k],evtZip[0][j][k])
            adcInp[i,j,:6] = adcInp[i,j,6]
    #Now this part of the code will get back the adc input necessary assuming a gain of 1:
    outFile = open("{0}_IAE_initialADCs.txt".format(filename),"w")
    #This returns the linearizer outputs for comparison
    outFileTwo = open("{0}_IAE_initialLins.txt".format(filename),"w")
    
    outFile.write("Put as initial values on input:\n")
    outFile.write("adcInit = [[[")
    outFileTwo.write("Check against the linearizer values in output:\n")
    outFileTwo.write("sol = [[[")
    for i,evADCSolZip in enumerate(zip(adcInp,sol)):
        if i> 0:
            outFile.write(",\n[[")
            outFileTwo.write(",\n[[")
        for j in range(300):
            if j>0:
                outFile.write(",\n[")
                outFileTwo.write(",\n[")

            for k in range(10):
                if k>0:
                    outFile.write(", ")
                    if k<4:
                        outFileTwo.write(", ")
                outFile.write(str(int("1{}".format(bin(evADCSolZip[0][j][k])[2:].zfill(12)),2)))
                if k<4:
                    outFileTwo.write(str(int("{}".format(bin(evADCSolZip[1][j][k])[2:].zfill(12)),2)))
            outFile.write("]")
            outFileTwo.write("]")
        outFile.write("]")
        outFileTwo.write("]")
    outFile.write("]")
    outFileTwo.write("]")
else:
    uniqueCoeffAr = [coeffAr[i] for i in range(0,1200,4)]
    adcInp = np.zeros((300,10),dtype = int)
    for i,cocryZip in enumerate(zip(uniqueCoeffAr,sol)):
        for j,linOut in enumerate(cocryZip[1]):
            adcInp[i,6+j] = LintoADC(linOut,cocryZip[0])
        adcInp[i][:6] = adcInp[i][6]
    #Now this part of the code will get back the adc input necessary assuming a gain of 1:
    outFile = open("{0}_initialADCs.txt".format(filename),"w")
    #This returns the linearizer outputs for comparison
    outFileTwo = open("{0}_initialLins.txt".format(filename),"w")
    outFile.write("Put as initial values on input:\n")
    outFile.write("adcInit = [["+str(int("1"+bin(adcInp[0][0])[2:].zfill(12),2))+", "+str(int("1"+bin(adcInp[0][1])[2:].zfill(12),2))+", "+str(int("1"+bin(adcInp[0][2])[2:].zfill(12),2))+", "+str(int("1"+bin(adcInp[0][3])[2:].zfill(12),2))+", "+str(int("1"+bin(adcInp[0][4])[2:].zfill(12),2))+", "+str(int("1"+bin(adcInp[0][5])[2:].zfill(12),2))+", "+str(int("1"+bin(adcInp[0][6])[2:].zfill(12),2))+", "+str(int("1"+bin(adcInp[0][7])[2:].zfill(12),2))+", "+str(int("1"+bin(adcInp[0][8])[2:].zfill(12),2))+", "+str(int("1"+bin(adcInp[0][9])[2:].zfill(12),2))+"]")
    outFileTwo.write("Check against the linearizer values in output:\n")
    outFileTwo.write("sol = [["+str(int(sol[0][0]))+", "+str(int(sol[0][1]))+", "+str(int(sol[0][2]))+", "+str(int(sol[0][3]))+"]")
    for ar,arSol in zip(adcInp[1:],sol[1:]):
        outFile.write(",\n["+str(int("1"+bin(ar[0])[2:].zfill(12),2)))
        outFileTwo.write(",\n["+str(int(arSol[0])))
        for i, element in enumerate(ar[1:]):
            j = i + 1
            outFile.write(", "+str(int("1"+bin(element)[2:].zfill(12),2)))
            if j < 4:
                outFileTwo.write(", "+str(int(arSol[j])))
        outFile.write("]")
        outFileTwo.write("]")
    outFile.write("]\n")
    outFileTwo.write("]\n")

outFile.close()
outFileTwo.close()
