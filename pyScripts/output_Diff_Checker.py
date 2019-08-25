#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 19:27:37 2019

@author: lutton
"""

#This code takes two input or output files and compares them to each other. Outputting the differences and their locations, if any.

import re
#This tells the program to only look at a certain number of links when comparing output and to ignore differences
#past linksToCheck
justFirst = False
linksToCheck = 48

#Turn to True if comparing input files instead of output files
inputCheck = False

#This was necessary when j was being added to the input
#essentially just discludes the first four bits of the meta data so that
#if one input file has j and the other doesn't then a difference won't be seen between the two
#so long as they are the same otherwise
ignoreJ = False

#For multiple events adds a counter for that
multipleEvents = True

#Place files to check here:
"""
filenameOne = "test2_28links_AddedGain_out_ref.txt"
filenameTwo = "outputs_dlutton_test2_65_inlined_28L11C_NewCo.txt"
"""
"""
filenameOne = "test2_100Events_300Channels__2evts_28links_inptest.txt"
filenameTwo = "test2_100Events_300Channels__2evts_28links_inp.txt"
"""

filenameOne = "test2_100Events_300Channels__8evts_28links_IAE_out_ref.txt"
filenameTwo = "test2_100Events_300Channels__8evts_28links_IAE_FromTPG_out_ref.txt"

#Stores three elements per difference: location, input from first file, input from second file
difArray = []
jPlusOne=0

#Tells you which crystals the difference is on
difCry = []

if multipleEvents:
    #Changes the j so that it's negative at the start if you have a fake initial Event
    initEvent = True
    if initEvent:
        evtCtr = -2
        jPlusOne = -10
    else:
        evtCtr = -1

with open(filenameOne) as inFileOne, open(filenameTwo) as inFileTwo:
    
    wrdCnt = 0
    
    for lineOne, lineTwo in zip(inFileOne, inFileTwo):
        lineArrayOne = re.split(r'[ \n]', lineOne)
        lineArrayTwo = re.split(r'[ \n]', lineTwo)
        #First checks that the files are formatted similarly. They should all have the same length on each line
        if (len(lineArrayOne) != len(lineArrayTwo)):
            print (len(lineArrayOne))
            print (len(lineArrayTwo))
            print (lineArrayOne)
            print (lineArrayTwo)
            print('This line is unequal in length:'+str(wrdCnt))
            break
        
        #Removing the spaces and line breaks from the array. NS=NoSpaces
        lineArrayOneNS = [x for x in lineArrayOne if x !=""]
        lineArrayTwoNS = [x for x in lineArrayTwo if x !=""]
        
        #Checking length again to make sure the same number of elements are in each array
        if (len(lineArrayOneNS) != len(lineArrayTwoNS)):
            print (len(lineArrayOneNS))
            print (len(lineArrayTwoNS))
            print (lineArrayOneNS)
            print (lineArrayTwoNS)
            print('This NS line is unequal in length:'+str(wrdCnt))
            break
        
        #Same as below, but only running over a fixed number of links
        if justFirst:
            if multipleEvents:
                print("not yet imp")
            #Min here is used because some of the first lines before input might be smaller than the linksToCheck
            for lnkPlusOne in range(min(linksToCheck+1,len(lineArrayOneNS))):
                if ignoreJ and lnkPlusOne > 0:
                    if (lineArrayOneNS[lnkPlusOne][:-1] != lineArrayTwoNS[lnkPlusOne][:-1]):
                        if inputCheck or wrdCnt < 30:
                            print(lineArrayOneNS[0]+"   "+lineArrayTwoNS[0])
                        difArray.append( str((jPlusOne-1,wrdCnt % 3,lnkPlusOne-1))+"    "+lineArrayOneNS[lnkPlusOne]+"    "+lineArrayTwoNS[lnkPlusOne] )
                elif (lineArrayOneNS[lnkPlusOne] != lineArrayTwoNS[lnkPlusOne]):
                        if inputCheck or wrdCnt < 30:
                            print(lineArrayOneNS[0]+"   "+lineArrayTwoNS[0])
                        difArray.append( str((jPlusOne-1,wrdCnt % 3,lnkPlusOne-1))+"    "+lineArrayOneNS[lnkPlusOne]+"    "+lineArrayTwoNS[lnkPlusOne] )
        
        #iterator is lnkPlusOne since it goes over the wordCount also
        else:
            for lnkPlusOne in range(len(lineArrayOneNS)):
                #Same as below just ignores the last character in each input
                if ignoreJ and lnkPlusOne > 0:
                    if multipleEvents:
                        print("not yet imp")
                    if (lineArrayOneNS[lnkPlusOne][:-1] != lineArrayTwoNS[lnkPlusOne][:-1]):
                        if inputCheck or wrdCnt < 30:
                            print(lineArrayOneNS[0]+"   "+lineArrayTwoNS[0])
                        difArray.append( str((jPlusOne-1,wrdCnt % 3,lnkPlusOne-1))+"    "+lineArrayOneNS[lnkPlusOne]+"    "+lineArrayTwoNS[lnkPlusOne] )
                
                
                elif (lineArrayOneNS[lnkPlusOne] != lineArrayTwoNS[lnkPlusOne]):
                    difCry = []
                    #I put wrdCnt < 30 here just to limit the amount of console output from running the program
                    #Don't remember why I made inputCheck skip this limit, but it's not important.
                    if inputCheck or wrdCnt < 30:
                        print(lineArrayOneNS[0]+"   "+lineArrayTwoNS[0])
                    #Getting which specific crystals are dif:
                    if lnkPlusOne == 0:
                        difCry = ["wrdCnt"]
                    else:
                        if wrdCnt % 3 == 0:
                            for i in range(3):
                                if lineArrayOneNS[lnkPlusOne][10-(4*i):14-(4*i)] != lineArrayTwoNS[lnkPlusOne][10-(4*i):14-(4*i)]:
                                    difCry.append(i)
                        else:
                            for i in range(4):
                                if lineArrayOneNS[lnkPlusOne][14-(4*i):18-(4*i)] != lineArrayTwoNS[lnkPlusOne][14-(4*i):18-(4*i)]:
                                    difCry.append(3+i+(4*((wrdCnt % 3)-1)))
                    #then how far into the specific crossing the difference is so on the first part wrdCnt %3 = 0, 2nd it =1, etc;
                    #Finally which link it's on, so if it's on link 00, lnkPlusOne-1 = 0)
                    if multipleEvents:
                        difArray.append( str((evtCtr,jPlusOne-1,wrdCnt % 3,lnkPlusOne-1,difCry))+"       "+lineArrayOneNS[lnkPlusOne]+"       "+lineArrayTwoNS[lnkPlusOne] )
                    else:
                        difArray.append( str((jPlusOne-1,wrdCnt % 3,lnkPlusOne-1,difCry))+"       "+lineArrayOneNS[lnkPlusOne]+"       "+lineArrayTwoNS[lnkPlusOne] )
        wrdCnt+=1
        if (wrdCnt % 3 == 0):
            jPlusOne += 1
            if (jPlusOne-1) % 10 == 0 and multipleEvents:
                evtCtr += 1
fileString = "{0}_{1}_diff".format(filenameOne,filenameTwo)

if inputCheck:
    fileString= fileString+"_IC"
else:
    fileString= fileString+"_OC"
if justFirst:
    fileString= fileString+"_JF"+str(linksToCheck)
if ignoreJ:
    fileString= fileString+"_Ij"
    
fileString = fileString+".txt"
outFile = open(fileString,"w")
outFile.write("location"+"                "+"fileOne"+"                "+"fileTwo"+"\n")
for dif in difArray:
    outFile.write(dif+"\n")
        
outFile.close()