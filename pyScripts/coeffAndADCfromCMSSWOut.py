#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 17:37:58 2019

@author: dylanlutton
"""

import re
import numpy as np


#Total number of links to write in
N_CHANNEL_IN = 48
#Total number of links to put actual input in
xLinks = 28
#Number of events to iterate through
nEvents = 2

inputName = "test2"
filename = "100Events_300Channels"

#The first input file Nancy gave is formatted differently; use this if you're looking at "Chain_withSignal_100evt"
chain = False
#For getting the linearizer, filter, and peak output as well
lFPOut = True

if lFPOut:
    """
    lOut = np.zeros((nEvents,300,10),dtype=int)
    fOut = np.zeros((nEvents,300,10),dtype=int)
    pOut = np.zeros((nEvents,300,10),dtype=int)
    lfpOut = [lOut,fOut,pOut]
    """
    lfpOut = np.zeros((3,nEvents,300,10),dtype=int)
    lfpIter = -1
    maxValAr= [0x30000,0x3FFFF,0x3FF]
    giveValAr = [0,0x3FFFF,0x3FF]
    
with open(filename) as inFile:
    #Keeps track of which event
    evtCtr = 0
    #Checks to see whether or not any events are skipped (e.g. event 2 to event 4 instead of 3)
    evttst = 0
    #Holds the coefficients for each crystal by their id
    coeffDict = {}
    #Holds the order of the ids
    numbDict = {}
    #Holds the order of the ids in reverse
    idDict = {}
    #used to skip over unnecessary lines
    skip = 0
    #Id of the crystal being looked at
    rawId = 0
    #Holds the number of unique crystals that have been run over. Shouldn't exceed 300
    cryCount = 0
    #Holds the coefficients in order after they've been accumulated
    coeffAr = []
    #Holds the input. dimensions: event, crystal, input number
    linkAr = np.zeros((nEvents,300,10),dtype=int)
    linkOAr = np.zeros((nEvents,300,10),dtype=int)
    #Used to differentiate between the input and the output part of the file
    out = False
    #Used to count which part of the input you're one when going over one crystal
    adcCount = 0
    #Used to check the consistency of coefficients across events
    tmpVal = ""
    #Used to cut off the outputs at the
    #Loop for the whole file
    for k,line in enumerate(inFile):
        #Skips however many lines are put into skip
        if skip > 0:
            skip = skip - 1
            continue
        
        #Gets the event number, checks that it's moving sequentially
        if "Treating event" in line:
            evttst = evtCtr
            evtCtr =  int(re.split(r'[ \n]', line)[5][:-1])
            if evtCtr > nEvents:
                break
            if evtCtr - evttst != 1:
                print("event skipping between {0} and {1}".format(evttst,evtCtr))
            if chain:
                coeffDict[evtCtr] = ["","",""]
                numbDict[cryCount] = evtCtr
            continue
        
        #Gets the id of the crystal, adds it to the coeffDict if it's not already present
        elif "*** Channel ***" in line:
            #Resetting out and adcCount
            out = False
            adcCount = 0
            if not chain:
                skip =1
            rawId = int(re.split(r'[ \n]', line)[7])
            if rawId not in coeffDict:
                coeffDict[rawId] = ["","",""]
                numbDict[cryCount] = rawId
                idDict[rawId] = cryCount
                cryCount += 1
                if cryCount > 300:
                    print("cryCount too highCount")
            lfpIter = -1
            continue
        
        #Skipping output for now. Add later
        elif "output" in line:
            lfpIter +=1
            out = True
            continue
        
        lineAr = re.split(r'[ \n]', line)
        
        #Checking if it's that first line of inputs.
        if chain and len(lineAr) == 12 and not out:
            if chain:
                print("not yet imp1")
            continue
        
        if out:
            if lfpIter == 3:
                for j,i in enumerate(range(1,20,2)):
                    if int(lineAr[i])> 1023:
                        linkOAr[evtCtr-1,idDict[rawId],j] = 1023
                    else:
                        linkOAr[evtCtr-1,idDict[rawId],j] = int(lineAr[i])
            else:
                for i in range(10):
                    if int(lineAr[i])> maxValAr[lfpIter]:
                        lfpOut[lfpIter,evtCtr-1,idDict[rawId],i] = giveValAr[lfpIter]
                    else:
                        lfpOut[lfpIter,evtCtr-1,idDict[rawId],i] = int(lineAr[i])
                    
        else:
            #Getting the gain
            gainVal = int(lineAr[0])
            #Getting the component parts of the coefficients
            coPed = hex(int(lineAr[2]))[2:].zfill(3)
            coShift = hex(int(lineAr[3]))[2:].zfill(1)
            coMult = hex(int(lineAr[4]))[2:].zfill(2)
            #Putting the coefficient together
            coFull = "0x{0}{1}{2}".format(coMult,coShift,coPed)
            #Getting the input number
            biNum = int(bin(gainVal)[2:].zfill(4)+bin(int(lineAr[1]))[2:].zfill(12),2)
            if chain:
                tmpVal = coeffDict[evtCtr][gainVal-1]
            else:
                tmpVal = coeffDict[rawId][gainVal-1]
                linkAr[evtCtr-1,idDict[rawId],adcCount] = biNum

            if tmpVal:
                if not coFull ==  tmpVal:
                    print("oh no")
                    print(k,tmpVal,coFull,rawId)
            else:
                if chain:
                    coeffDict[evtCtr][gainVal-1] = coFull
                else:
                    #Adding the coefficient to the dictionary
                    coeffDict[rawId][gainVal-1] = coFull
            adcCount +=1
        
if chain:
    coeffAr = [coeffDict[x] for x in coeffDict if coeffDict[x] != ["","",""]]

#Adding, in order, the coefficients to an array.
else:
    for i in range(300):
        coeffAr.append(coeffDict[numbDict[i]])
        



outFile = open("{0}_{1}__{2}evts_{3}links_inp.txt".format(inputName,filename,nEvents,xLinks),"w")
outFileTwo = open("{0}_{1}__{2}evts_{3}links_out_ref.txt".format(inputName,filename,nEvents,xLinks),"w")

j=0

#Opens the reference input file to get the header stuff
with open("{0}_inp.txt".format(inputName)) as inFile:
    for k,line in enumerate(inFile):
        if k >= 3:
            break
        outFile.write(line)
outFileTwo.write("===================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================== \nWordCnt             LINK_00               LINK_01               LINK_02               LINK_03               LINK_04               LINK_05               LINK_06               LINK_07               LINK_08               LINK_09               LINK_10               LINK_11               LINK_12               LINK_13               LINK_14               LINK_15               LINK_16               LINK_17               LINK_18               LINK_19               LINK_20               LINK_21               LINK_22               LINK_23               LINK_24               LINK_25               LINK_26               LINK_27               LINK_28               LINK_29               LINK_30               LINK_31               LINK_32               LINK_33               LINK_34               LINK_35               LINK_36               LINK_37               LINK_38               LINK_39               LINK_40               LINK_41               LINK_42               LINK_43               LINK_44               LINK_45               LINK_46               LINK_47 \n#BeginData\n")

wrdCnt = 0
for ev,evOut in zip(linkAr,linkOAr):
    for i in range(10):
        inpAr = ["0000"]*48
        outAr = ["0000"]*48
        for k in range(48):
            for l in range(11):
                if (k*11+l) < 300:
                    inpAr[k] = hex(ev[k*11+l][i])[2:].zfill(4)+inpAr[k]
                    outAr[k] = hex(evOut[k*11+l][i])[2:].zfill(4)+outAr[k]
                else:
                    inpAr[k] = "0000"+inpAr[k]
                    outAr[k] = "0000"+outAr[k]
        for j in range(3):
            outFile.write("{0:#0{1}x}   ".format(wrdCnt,6))
            outFileTwo.write("{0:#0{1}x}   ".format(wrdCnt,6))
            for lnk,lnkOut in zip(inpAr,outAr):
                outFile.write("0x"+lnk[32-(16*j):48-(16*j)]+"    ")
                outFileTwo.write("0x"+lnkOut[32-(16*j):48-(16*j)]+"    ")
               
            outFile.write("\n")
            outFileTwo.write("\n")
            wrdCnt +=1

outFile.write("\n")
outFile.close()
outFileTwo.close()

outFile = open("{0}_{1}_{2}coeffAr.txt".format(inputName,filename,xLinks),"w")
outFile.write("C coeff:\n")
outFile.write("static const uint24_t coeff[300][3] = {{"+coeffAr[0][0]+", "+"0x0"+", "+"0x0"+"}")
for ar in coeffAr[1:]:
    outFile.write(",\n{"+ar[0])
    for element in ar[1:]:
        outFile.write(", "+"0x0")
    outFile.write("}")
outFile.write("};\n")
            
outFile.write("Python coeff:\n")
outFile.write("coeff = [["+coeffAr[0][0]+", "+"0x0"+", "+"0x0"+"]")
for ar in coeffAr[1:]:
    outFile.write(",\n["+ar[0])
    for element in ar[1:]:
        outFile.write(", "+"0x0")
    outFile.write("]")
outFile.write("]\n")    

outFile.close()

nameAr = ["linOut","filtOut"]
outFile = open("reg_out_{}_{}evts_{}links.txt".format(filename,nEvents,xLinks),"w")
for ev in range(nEvents):
    outFile.write("ev "+str(ev)+"\n")
    for i in range(10):
        outFile.write("adc "+str(i)+"\n")
        for cry in range(300):
            outFile.write("crystal "+str(cry)+"\n")
            for j in range(3):
                if i <3:
                    if j == 2:
                        if i ==0:
                            outFile.write("peakOut "+str(lfpOut[j,ev,cry,i])+" 0")
                        else:
                            outFile.write("peakOut "+str(lfpOut[j,ev,cry,i])+" "+str(lfpOut[j,ev,cry,i-1]))
                    else:
                        outFile.write(str(nameAr[j]))
                        for k in range(i+1):
                            outFile.write(" "+str(lfpOut[j,ev,cry,i-k]))
                        for k in range(3-i):
                            outFile.write(" "+"0")
                else:
                    if j ==2:
                        outFile.write("peakOut "+str(lfpOut[j,ev,cry,i])+" "+str(lfpOut[j,ev,cry,i-1]))
                    else:
                        outFile.write(str(nameAr[j])+" "+str(lfpOut[j,ev,cry,i])+" "+str(lfpOut[j,ev,cry,i-1])+" "+str(lfpOut[j,ev,cry,i-2])+" "+str(lfpOut[j,ev,cry,i-3]))

                outFile.write("\n")

outFile.close()

