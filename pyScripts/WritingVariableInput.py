#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created in Jul 2019

@author: lutton
"""

import re

#This program generates input given a variable number of channels in and links to run over. At current it assumes 11 crystals
#per link and that you're running over each.

#If addGain is on, the input will have a "1" at the start of each crystal that isn't giving real input (so 0000 goes to 1000).
addGain = True
#Total number of links to write in
N_CHANNEL_IN = 48
inputName = "test2"
#Total number of links to put actual input in
xLinks = 28
if addGain:
    outFile = open("{0}_{1}links_AddedGain_inp.txt".format(inputName,xLinks),"w")
else:
    outFile = open("{0}_{1}links_inp.txt".format(inputName,xLinks),"w")

j=0

#Opens the reference input file
with open("{0}_inp.txt".format(inputName)) as inFile:
    wrdCnt = 0
    for k,lineOne in enumerate(inFile):
        
        #Skipping the header stuff
        if k < 3:
            outFile.write(lineOne)
            
        else:
            if k != 3:
                outFile.write("\n")
                
            outFile.write("{0:#0{1}x}   ".format(wrdCnt,6))
            
            #At the moment, since the reference file only has actual input in the first 64 bits of each link
            #only the first of each 3 word counts is pulled from.
            if wrdCnt % 3 == 0:
                
                #Removing all spaces and \n from the line taken in and then
                #creating the link_in array from each input excluding the wordCount.
                lineArray = re.split(r'[ \n]', lineOne)
                link_in = [x for x in lineArray[1:] if x !=""]
                
                #Running over the links up to the requested number
                for lnk in range(xLinks):
                    #Adds the gain in the appropriate places, skipping over the actual input
                    if addGain:
                        outFile.write(link_in[lnk][:2]+"1"+link_in[lnk][3:10]+"1"+link_in[lnk][11:]+"    ")
                    else:
                        outFile.write(link_in[lnk]+"    ")
                    
            #If not an input part of the link just writes the standard no-input for each
            else:
                for lnk in range(xLinks):
                    if addGain:
                        outFile.write("0x1000100010001000    ")
                    else:
                        outFile.write("0x0000000000000000    ")
                        
            #Just zeros for all links outside of what is run over.
            for lnk in range(xLinks,N_CHANNEL_IN):
                outFile.write("0x0000000000000000    ")
            wrdCnt+=1
outFile.write("\n")    
          
outFile.close()