#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 17:37:58 2019

@author: dylanlutton
"""

import re
import numpy as np
from WritingOutputRef_VariableLinks import TPG 
from WritingOutputRef_VariableLinks import registers
from adcAndSol import adcInitAr
from adcAndSol import solInitAr



#These are the correct ADCs to add to the in
#Total number of links to write in
N_CHANNEL_IN = 48
#Total number of links to put actual input in
xLinks = 28
#Number of events to iterate through
nEvents = 8
#Limit on number of crystals to consider for inp/output:
maxCrystals = 300

sol = solInitAr[:nEvents]
adcInit = adcInitAr[:nEvents]

#Only output the registers from one crystal for testing
outOneCrystal = False
if outOneCrystal: #Sets crystal to output
    outCry = 7


inputName = "test2"
filename = "100Events_300Channels"

#The first input file Nancy gave is formatted differently; use this if you're looking at "Chain_withSignal_100evt"
#Won't work rn because of changes I made to the coeffDict and how it outputs to the output file
chain = False
#For getting the linearizer, filter, and peak output as well
lFPOut = True
#Working under the assumption that one event leads into the next, so that
#the formatter and peak reg from one event will follow into the next
eventsTouch = False

#Number of Crystals per Link
NCrystalsPerLink = 11
#Starts with a constructed "Event" that is just the first input of each crystal to initialize the registers
initEvent = True
if initEvent: #Setting initAllEvents and initializing the gain array
    #Do this for every event
    initAllEvents = True
    #Holds the gains corresponding to the first input to each crystal for use in initEvent
    gainAr = []



    #Converting array to hexlinks for writing input file
    adcInitLinkAr = []
    if initAllEvents:
        for ev in adcInit:
            adcEvLinkAr = []
            for i in range(10):
                adcInitLink = ["0000"]*48
    
                for j in range(xLinks):
                    for k in range(11):
                        cryCount = (j*11)+k
                        if cryCount >= 300:
                            adcInitLink[j] = "0000"+adcInitLink[j]
                        else:
                            adcInitLink[j] = hex(ev[cryCount][i])[2:].zfill(4)+adcInitLink[j]
                for j in range(xLinks,48,1):
                    
                    adcInitLink[j] = "00000000000000000000000000000000000000000000"+adcInitLink[j]
                    #adcInitLink[j] = "0x"+adcInitLink[j]
                adcEvLinkAr.append(adcInitLink)
            adcInitLinkAr.append(adcEvLinkAr)

    else:
        for i in range(10):
            adcInitLink = ["0000"]*48
    
            for j in range(xLinks):
                for k in range(11):
                    cryCount = (j*11)+k
                    if cryCount >= 300:
                        adcInitLink[j] = "0000"+adcInitLink[j]
                    else:
                        adcInitLink[j] = hex(adcInit[cryCount][i])[2:].zfill(4)+adcInitLink[j]
            for j in range(xLinks,48,1):
                
                adcInitLink[j] = "00000000000000000000000000000000000000000000"+adcInitLink[j]
                #adcInitLink[j] = "0x"+adcInitLink[j]
            adcInitLinkAr.append(adcInitLink)
            
                
if lFPOut: #Initializing the variables for outputting the lfp
    lfpOut = np.zeros((3,nEvents,maxCrystals,10),dtype=int)
    lfpIter = 0
    maxValAr= [0x30000,0x3FFFF,0x3FF]
    giveValAr = [0,0x3FFFF,0x3FF]
    

with open(filename) as inFile: #Main thing
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
    if eventsTouch: #If the events are assumed to touch, then need to save things between them
        filterSave = [0]*3
        outSave = [0]*2
        chckNTimes = 0
        crySave = 0
        weights = [24, 31, 16, -35, -36]
    chckEventWall = False

    #Used to cut off the outputs at the
    #Loop for the whole file
    for k,line in enumerate(inFile): #Main input loop to fill the arrays
        #Skips however many lines are put into skip
        if skip > 0: #Skipping skip number of lines
            skip = skip - 1
            continue
        
        #Gets the event number, checks that it's moving sequentially
        if "Treating event" in line: #Sets evtCtr from file
            evttst = evtCtr
            evtCtr =  int(re.split(r'[ \n]', line)[5][:-1])
            if evtCtr > nEvents: #For breaking
                break
            if evtCtr - evttst != 1: #Just checking for weird skipping
                print("event skipping between {0} and {1}".format(evttst,evtCtr))
            if chain: #for setting coeffDict and numbDict
                coeffDict[evtCtr] = ["","",""]
                numbDict[cryCount] = evtCtr
            continue
        
        #Gets the id of the crystal, adds it to the coeffDict if it's not already present
        elif "*** Channel ***" in line: # Resetting/updating some variables,adding Id to dict
            #Resetting out and adcCount
            out = False
            adcCount = 0
            if not chain: #skipping useless line
                skip =1
            rawId = int(re.split(r'[ \n]', line)[7])
            if rawId not in coeffDict:
                coeffDict[rawId] = ["0x0","0x0","0x0"]
                numbDict[cryCount] = rawId
                idDict[rawId] = cryCount
                cryCount += 1
                if cryCount > maxCrystals:
                    print("cryCount too highCount")
            lfpIter = 0
            continue
        
        elif "output" in line: #Starting the output section
            out = True
            continue
        
        lineAr = re.split(r'[ \n]', line)
        
        #Checking if it's that first line of inputs.
        if chain and len(lineAr) == 12 and not out:
            if chain:
                print("not yet imp1")
            continue
        
        if out: #Getting all outputs to add to LinkOAr and lfpOut
            if lfpIter == 3: #Getting the formatter output
                #linkOAr[evtCtr-1,idDict[rawId],0] = outSave[0]
                #linkOAr[evtCtr-1,idDict[rawId],1] = outSave[1]
                for j,i in enumerate(range(1,16,2)): #Looping over each output and bit shifting >> 2
                    tmpVar = int(lineAr[i]) >> 2
                    if tmpVar > 1023: #out 1023 if it's too big
                        linkOAr[evtCtr-1,idDict[rawId],j+2] = 1023
                    else: #otherwise just set linkOAr to what's given
                        linkOAr[evtCtr-1,idDict[rawId],j+2] = tmpVar
                """
                outSave[1] = int(lineAr[17]) >> 2
                outSave[0] = int(lineAr[19]) >> 2
                for x in outSave:
                    if x != 0 and idDict[rawId] <11:
                        print("wuhh",evtCtr,idDict[rawId],outSave)
                        chckEventWall = True
                        chckNTimes += 1
                        crySave =idDict[rawId]
                """
                        

            else: #All outputs previous to formatter
                if (lfpIter == 0): #For the linearizer
                    for i in range(10): #Looping over each linOut
                        if int(lineAr[i])> maxValAr[lfpIter]: #If too big give specific value
                            lfpOut[lfpIter,evtCtr-1,idDict[rawId],i] = giveValAr[lfpIter]
                        else: #Otherwise just give the value in input
                            lfpOut[lfpIter,evtCtr-1,idDict[rawId],i] = int(lineAr[i])
                elif (lfpIter == 1): #Filter
                    for i in range(9): #Looping over each filOut
                        if int(lineAr[i])> maxValAr[lfpIter]: #if too big
                            lfpOut[lfpIter,evtCtr-1,idDict[rawId],i+1] = giveValAr[lfpIter]
                            if eventsTouch: #If the events touch you want to save some
                                filterSave[0] = giveValAr[lfpIter]
                        else: #just get the value from input
                            lfpOut[lfpIter,evtCtr-1,idDict[rawId],i+1] = int(lineAr[i])
                            if eventsTouch: #same
                                filterSave[0] = int(lineAr[9])
                    
                    #Don't care about this anymore
                    if chckEventWall and idDict[rawId] == crySave: #This was just some stuff for checking if events really touched
                        acc = 0
                        acc += (lfpOut[0,evtCtr-1,crySave,0]*weights[0]) >> 6
                        for x,y in zip(weights[1:],lfpOut[0,evtCtr-2,crySave,6:]):
                            acc += (x*y) >> 6
                        print(acc,filterSave[0])
                        print(lfpOut[1,evtCtr-2,crySave])
                        chckNTimes -= 1
                        if chckNTimes == 0:
                            chckEventWall = False
                            
                else: #Getting peakOut
                    for i in range(8): #Loop over the input 
                        if int(lineAr[i])> maxValAr[lfpIter]: #If too big get dif value
                            lfpOut[lfpIter,evtCtr-1,idDict[rawId],i+2] = giveValAr[lfpIter]
                        else: #Else just take inp
                            lfpOut[lfpIter,evtCtr-1,idDict[rawId],i+2] = int(lineAr[i])

                lfpIter +=1
                skip = 1
                    
        else: #Get the gain, coefficients, and input
            #Getting the gain
            gainVal = int(lineAr[0])
            if initEvent: #Putting the gainVal into the gainAr
                if len(gainAr) < maxCrystals: #But only for the first evt
                    gainAr.append(gainVal)
            #Getting the component parts of the coefficients
            coPed = hex(int(lineAr[2]))[2:].zfill(3)
            coShift = hex(int(lineAr[3]))[2:].zfill(1)
            coMult = hex(int(lineAr[4]))[2:].zfill(2)
            #Putting the coefficient together
            coFull = "0x{0}{1}{2}".format(coMult,coShift,coPed)
            #Getting the input number
            biNum = int(bin(gainVal)[2:].zfill(4)+bin(int(lineAr[1]))[2:].zfill(12),2)
            if chain: #Getting the coeff to check if it's 0x0 or needs to be filled
                tmpVal = coeffDict[evtCtr][gainVal-1]
            else: #Getting the coeff and  setting the linkAr
                tmpVal = coeffDict[rawId][gainVal-1]
                linkAr[evtCtr-1,idDict[rawId],adcCount] = biNum

            if tmpVal != "0x0": #If the coeff is already in, doesn't need to be reset
                if not coFull ==  tmpVal: #But if it's different that's bad
                    print("oh no")
                    print(k,tmpVal,coFull,rawId)
            else: #If the coeff isn't in, then set the coeff
                if chain: #set w/ evtCtr
                    coeffDict[evtCtr][gainVal-1] = coFull
                else: #set w/ rawId
                    #Adding the coefficient to the dictionary
                    coeffDict[rawId][gainVal-1] = coFull
            adcCount +=1
        
if chain: #Making coeff array while removing trash arrays
    coeffAr = [coeffDict[x] for x in coeffDict if coeffDict[x] != ["","",""]]

#Adding, in order, the coefficients to an array.
else: #Making coeff array
    for i in range(300): #Loop over the coeffDict to set array
        coeffAr.append(coeffDict[numbDict[i]])
        


if initEvent: #Opening file
    if eventsTouch:
        outFile = open("{0}_{1}__{2}evts_{3}links_IE_ET_inp.txt".format(inputName,filename,nEvents,xLinks),"w")
        outFileTwo = open("{0}_{1}__{2}evts_{3}links_IE_ET_out_ref.txt".format(inputName,filename,nEvents,xLinks),"w")
    if initAllEvents:
        outFile = open("{0}_{1}__{2}evts_{3}links_IAE_inp.txt".format(inputName,filename,nEvents,xLinks),"w")
        outFileTwo = open("{0}_{1}__{2}evts_{3}links_IAE_out_ref.txt".format(inputName,filename,nEvents,xLinks),"w")
    else:
        outFile = open("{0}_{1}__{2}evts_{3}links_IE_inp.txt".format(inputName,filename,nEvents,xLinks),"w")
        outFileTwo = open("{0}_{1}__{2}evts_{3}links_IE_out_ref.txt".format(inputName,filename,nEvents,xLinks),"w")
else: #Opening file dif name
    outFile = open("{0}_{1}__{2}evts_{3}links_inp.txt".format(inputName,filename,nEvents,xLinks),"w")
    outFileTwo = open("{0}_{1}__{2}evts_{3}links_out_ref.txt".format(inputName,filename,nEvents,xLinks),"w")

j=0

#Opens the reference input file to get the header stuff
with open("{0}_inp.txt".format(inputName)) as inFile: #Writing the header bits of inp from old inp file
    for k,line in enumerate(inFile):
        if k >= 3:
            break
        outFile.write(line)
        
outFileTwo.write("===================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================== \nWordCnt             LINK_00               LINK_01               LINK_02               LINK_03               LINK_04               LINK_05               LINK_06               LINK_07               LINK_08               LINK_09               LINK_10               LINK_11               LINK_12               LINK_13               LINK_14               LINK_15               LINK_16               LINK_17               LINK_18               LINK_19               LINK_20               LINK_21               LINK_22               LINK_23               LINK_24               LINK_25               LINK_26               LINK_27               LINK_28               LINK_29               LINK_30               LINK_31               LINK_32               LINK_33               LINK_34               LINK_35               LINK_36               LINK_37               LINK_38               LINK_39               LINK_40               LINK_41               LINK_42               LINK_43               LINK_44               LINK_45               LINK_46               LINK_47 \n#BeginData\n")
if initEvent: #Setting the amount necessary to repeat writing out for initEvent and initializing spStart
    repeatNTimes = 10
    spStart = np.zeros((nEvents,13,maxCrystals,2),dtype=int)

else: #setting it to not repeat
    repeatNTimes = 0
wrdCnt = 0
evtCtr = 0
reg = [[registers() for y in range(NCrystalsPerLink)] for x in range(xLinks)]

for ev,evOut in zip(linkAr,linkOAr):#Looping over the linkin/out arrays
        #Looping over the first input ten times and running the TPG on it for output
        #Above comment maybe outdated. this loop happens on i ==0
        #and writes
    if repeatNTimes > 0 and initEvent: #start of initEvent

        for l in range(repeatNTimes): #main initEvent Loop 
            tempus = False
            tingsu = False
            startAr = adcInit[:]
            tmpAr = ["000000000000000000000000000000000000000000000000"]*48
            for k in range(xLinks): #Main loop over all links in xLinks
                tmpOut = "0000"
                for u in range(NCrystalsPerLink): #Main loop over all crystals on links
                    cryCount = k*11+u
                    if cryCount >= 300: #For outputting zeros
                        tmpOut = "0000"+tmpOut
                    else: #For running TPG to get output
                        if (l == 3 or l == 4) and cryCount == 0: #Just for testing
                            tempus = True
                            tingsu = True
                        tmpOut = TPG(startAr[evtCtr][cryCount][l],int(coeffAr[cryCount][0],16),reg[k][u],tempus)+tmpOut
                        if l <= 6: #This whole bit is just checking the result
                            if (reg[k][u].shift_reg[0] != (sol[evtCtr][cryCount][0])):
                                print("AAAAAAAAAAAAAAAAAAAAAAAA NOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
                                print(reg[k][i].shift_reg)
                                print(adcInit[evtCtr][cryCount])
                                print([(x & 0xFFF) for x in adcInit[evtCtr][cryCount]])
                                print(sol[evtCtr][cryCount])
                                print(l,k,u,cryCount)
                                print("AAAAAAAAAAAAAAAAAAAAAAAA NOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
                        else:  #same with this
                            if (reg[k][u].shift_reg[0] != (sol[evtCtr][cryCount][l-6])):
                                print("AAAAAAAAAAAAAAAAAAAAAAAA NOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
                                print(reg[k][u].shift_reg)
                                print(adcInit[evtCtr][cryCount])
                                print([(x & 0xFFF) for x in adcInit[evtCtr][cryCount]])
                                print(sol[evtCtr][cryCount])
                                print(l,k,u,cryCount)
                                print("AAAAAAAAAAAAAAAAAAAAAAAA NOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
                        if tempus: #and this
                            print(tmpOut)
                            tempus = False
                        
                        spStart[evtCtr,l+3,cryCount,0] = reg[k][u].shift_reg[0]
                        spStart[evtCtr,l+1,cryCount,1] = reg[k][u].peak_reg[0]
                tmpAr[k] = tmpOut
                if tingsu: #just checking output
                    print(tmpAr[k])
                    tingsu = False
            for j in range(3): #Loop over three wrdCnts to write the output from repeatNTimes
                outFile.write("{0:#0{1}x}   ".format(wrdCnt,6))
                outFileTwo.write("{0:#0{1}x}   ".format(wrdCnt,6))
                for lnk,lnkOut in zip(adcInitLinkAr[evtCtr][l],tmpAr): #loop over each link to write the output
                    outFile.write("0x"+lnk[32-(16*j):48-(16*j)]+"    ")
                    outFileTwo.write("0x"+lnkOut[32-(16*j):48-(16*j)]+"    ")
                outFile.write("\n")
                outFileTwo.write("\n")
                wrdCnt +=1
            
    for i in range(10): #loop over each ten parts of event
        
        inpAr = ["0000"]*48
        outAr = ["0000"]*48
        for k in range(xLinks): #Filling inpAr/outAr on each link in xLinks
            for l in range(11): #and each crystal
                cryCount = (k*11)+l
                if cryCount < maxCrystals: #Fill from ev and evOut
                    inpAr[k] = hex(ev[cryCount][i])[2:].zfill(4)+inpAr[k]
                    outAr[k] = hex(evOut[cryCount][i])[2:].zfill(4)+outAr[k]
                        
                    if initAllEvents: #Adding the linout and formatter from the last parts of this event to the registers
                        for j in range(4): 
                            reg[k][l].shift_reg[j] =lfpOut[0,evtCtr,cryCount,9-j] 
                            if j <2:
                                reg[k][l].peak_reg[j] = lfpOut[1,evtCtr,cryCount,9-j] 

                else: #Just add zeros
                    inpAr[k] = "0000"+inpAr[k]
                    outAr[k] = "0000"+outAr[k]


        for k in range(xLinks,48,1): #Fill the rest with 0's
            inpAr[k] = "000000000000000000000000000000000000000000000000"
            outAr[k] = "000000000000000000000000000000000000000000000000"
        

                        


        for j in range(3): #Loop over 3 wrdCntsto write output from regular stuff
            outFile.write("{0:#0{1}x}   ".format(wrdCnt,6))
            outFileTwo.write("{0:#0{1}x}   ".format(wrdCnt,6))
            for lnk,lnkOut in zip(inpAr,outAr): #Loop over each link to write the output
                outFile.write("0x"+lnk[32-(16*j):48-(16*j)]+"    ")
                outFileTwo.write("0x"+lnkOut[32-(16*j):48-(16*j)]+"    ")
                

                   
            outFile.write("\n")
            outFileTwo.write("\n")
            wrdCnt +=1
    evtCtr += 1

outFile.close()
outFileTwo.close()


outFile = open("{0}_{1}_{2}coeffAr.txt".format(inputName,filename,xLinks),"w")
outFile.write("C coeff:\n")
outFile.write("static const uint24_t coeff[300][3] = {{"+coeffAr[0][0]+", "+coeffAr[0][1]+", "+coeffAr[0][2]+"}")

for ar in coeffAr[1:]: #Looping over the coeff arrays to write the coeff output file in C++
    outFile.write(",\n{"+ar[0])
    for element in ar[1:]: #Main loop over coefficients
        outFile.write(", "+element)
    outFile.write("}") 
outFile.write("};\n")
            
outFile.write("Python coeff:\n")
outFile.write("coeff = [["+coeffAr[0][0]+", "+coeffAr[0][1]+", "+coeffAr[0][2]+"]")
for ar in coeffAr[1:]: #Same but python
    outFile.write(",\n["+ar[0])
    for element in ar[1:]: #Same but python
        outFile.write(", "+element)
    outFile.write("]")
outFile.write("]\n")

outFile.close()

nameAr = ["linOut","peakOut"]
if initEvent: #Opening the reg_out file
    if eventsTouch:
        outFile = open("reg_out_{}_{}evts_{}links_IE_ET.txt".format(filename,nEvents,xLinks),"w")
    elif initAllEvents:
        outFile = open("reg_out_{}_{}evts_{}links_IAE.txt".format(filename,nEvents,xLinks),"w")
    else:
        outFile = open("reg_out_{}_{}evts_{}links_IE.txt".format(filename,nEvents,xLinks),"w")
else:
    outFile = open("reg_out_{}_{}evts_{}links.txt".format(filename,nEvents,xLinks),"w")

if outOneCrystal: #Printing some output
    print("Crystal "+str(outCry)+":")
if initEvent: #Starting output for initEvent regout at ev == -1
    outFile.write("ev -1\n")
    if outOneCrystal: #Printing some output
        print("ev -1")
    for i in range(10): #main loop over the 10 parts of event
        outFile.write("adc "+str(i)+"\n")
        for cry in range(min((xLinks*NCrystalsPerLink),maxCrystals)): #main loop over the crystals
            outFile.write("crystal "+str(cry)+"\n")
            outFile.write("shiftReg ")
            if outOneCrystal and cry == outCry: #printing some output
                print("crystal "+str(cry)+" adc "+str(i))
                print("shiftReg ",end="")
            for j in range(4): #write the shift register
                outFile.write(str(spStart[0,(i+3)-j,cry,0])+" ")
                if outOneCrystal and cry == outCry: #printing some output
                    print(str(spStart[0,(i+3)-j,cry,0]),end=" ")
            outFile.write("\n")
            outFile.write("peakReg ")
            if outOneCrystal and cry == outCry: #printing some output
                print("")
                print("peakReg ",end="")
            for j in range(2): #write the formatter output
                outFile.write(str(spStart[0,(i+1)-j,cry,1])+" ")
                if outOneCrystal and cry == outCry: #printing some output
                    print(str(spStart[0,(i+1)-j,cry,1]),end=" ")
            outFile.write("\n")
            if outOneCrystal and cry == outCry: #printing some output
                print("")

evPlusCtr = 0
for ev in range(nEvents): #main loop over events
    outFile.write("ev "+str(ev+evPlusCtr)+"\n")
    if outOneCrystal: #printing some output
        print("ev "+str(ev+evPlusCtr))
    for i in range(10): #main loop over 10 parts of each event
        outFile.write("adc "+str(i)+"\n")
        if outOneCrystal: #printing some output
            print("adc "+str(i))
        for cry in range(min((xLinks*NCrystalsPerLink),maxCrystals)): #main loop over crystals
            outFile.write("crystal "+str(cry)+"\n")
            if outOneCrystal and cry == outCry: #printing some output
                print("crystal "+str(cry))
            for j in range(3): #looping over lfp
                if initEvent: #Difference is carrying over lfp arrays from spStart
                    if i < 3: # Need to use spStart for the first 3
                        if j == 2: #spStart not relevant for peakOut
                            if i == 0: #putting ? because peakOut not gotten in fakeevent
                                outFile.write("actOut "+str(lfpOut[j,ev,cry,i])+" ?")
                                if outOneCrystal and cry == outCry: #printing some output
                                    print("actOut "+str(lfpOut[j,ev,cry,i])+" ?")
                            else: #or just writing as normal
                                outFile.write("actOut "+str(lfpOut[j,ev,cry,i])+" "+str(lfpOut[j,ev,cry,i-1]))
                                if outOneCrystal and cry == outCry: #printing some output
                                    print("actOut "+str(lfpOut[j,ev,cry,i])+" "+str(lfpOut[j,ev,cry,i-1]))
                        else: #writing lin and filt out
                            outFile.write(str(nameAr[j]))
                            if j == 0: #linout
                                if outOneCrystal and cry == outCry: #printing some output
                                    print(str(nameAr[j]),end="")
                                for k in range(i+1): #in this range don't need spStart
                                    outFile.write(" "+str(lfpOut[j,ev,cry,i-k]))
                                    if outOneCrystal and cry == outCry: #printing some output
                                        print(" "+str(lfpOut[j,ev,cry,i-k]),end="")
                                for k in range(3-i): #using spStart
                                    outFile.write(" "+str(spStart[ev][-k-1][cry][0]))
                                    if outOneCrystal and cry == outCry: #printing some output
                                        print(" "+str(spStart[ev][-k-1][cry][0]),end="")
                            else: #filtout
                                if outOneCrystal and cry == outCry: #printing some output
                                    print(str(nameAr[j]),end="")
                                for k in range(i+1): #don't near spStart in this range
                                    outFile.write(" "+str(lfpOut[j,ev,cry,i-k]))
                                    if outOneCrystal and cry == outCry: #printing some output
                                        print(" "+str(lfpOut[j,ev,cry,i-k]),end="")
                                for k in range(3-i): #using spStart
                                    outFile.write(" "+str(spStart[ev][-k-1][cry][1]))
                                    if outOneCrystal and cry == outCry: #printing some output
                                        print(" "+str(spStart[ev][-k-1][cry][1]),end="")
                            if outOneCrystal and cry == outCry: #printing some output
                                print("")
                    else: #Don't need spStart past this point
                        if j == 2: #peakout
                            outFile.write("actOut "+str(lfpOut[j,ev,cry,i])+" "+str(lfpOut[j,ev,cry,i-1]))
                            if outOneCrystal and cry == outCry: #printing some output
                                print("actOut "+str(lfpOut[j,ev,cry,i])+" "+str(lfpOut[j,ev,cry,i-1]))
                        else: #lin and filt out
                            outFile.write(str(nameAr[j])+" "+str(lfpOut[j,ev,cry,i])+" "+str(lfpOut[j,ev,cry,i-1])+" "+str(lfpOut[j,ev,cry,i-2])+" "+str(lfpOut[j,ev,cry,i-3]))
                            if outOneCrystal and cry == outCry: #printing some output
                                print(str(nameAr[j])+" "+str(lfpOut[j,ev,cry,i])+" "+str(lfpOut[j,ev,cry,i-1])+" "+str(lfpOut[j,ev,cry,i-2])+" "+str(lfpOut[j,ev,cry,i-3]))


                else: #Trash you don't do if initEvent is happening
                    if outOneCrystal:
                        print("not yet imp")
                    if i <3:
                        if j == 2:
                            if i ==0:
                                outFile.write("actOut "+str(lfpOut[j,ev,cry,i])+" 0")
                                
                            else:
                                outFile.write("actOut "+str(lfpOut[j,ev,cry,i])+" "+str(lfpOut[j,ev,cry,i-1]))
                        else:
                            outFile.write(str(nameAr[j]))
                            for k in range(i+1):
                                outFile.write(" "+str(lfpOut[j,ev,cry,i-k]))
                            for k in range(3-i):
                                outFile.write(" "+"0")
                    else:
                        if j ==2:
                            outFile.write("actOut "+str(lfpOut[j,ev,cry,i])+" "+str(lfpOut[j,ev,cry,i-1]))
                        else:
                            outFile.write(str(nameAr[j])+" "+str(lfpOut[j,ev,cry,i])+" "+str(lfpOut[j,ev,cry,i-1])+" "+str(lfpOut[j,ev,cry,i-2])+" "+str(lfpOut[j,ev,cry,i-3]))
                            
                outFile.write("\n")
    if initAllEvents and ev < nEvents - 1: #Starting output for initEvent regout at ev == ev+evPlusCtr+1
        outFile.write("fev {}\n".format(ev+evPlusCtr+1))
        for i in range(10): #main loop over the 10 parts of event
            outFile.write("adc "+str(i)+"\n")
            for cry in range(min((xLinks*NCrystalsPerLink),maxCrystals)): #main loop over the crystals
                outFile.write("crystal "+str(cry)+"\n")
                outFile.write("shiftReg ")
                for j in range(4): #write the shift register
                    outFile.write(str(spStart[ev+1,(i+3)-j,cry,0])+" ")
                outFile.write("\n")
                outFile.write("peakReg ")
                for j in range(2): #write the formatter output
                    outFile.write(str(spStart[ev+1,(i+1)-j,cry,1])+" ")
                outFile.write("\n")

outFile.close()

