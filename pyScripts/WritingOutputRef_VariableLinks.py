#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 19:27:37 2019

@author: lutton
"""

#This program returns output for given input in the same way that the TPG code does
#so that hardware output can be checked against this.
#Last I checked this gave both identical output for each crystal and identical register outputs for each crystal that is
#given actual input with the standard input file for all 48 links as from HLS csim.
#Would need to be changed if, for instance, the specific crystal that is receiving input each link is changed.

import re

#Number of links to run over and get output from.
xLinks = 28

#addGain here is just to select the right input filename
addGain = True
if addGain:
    filename = "test2_{}links_AddedGain".format(xLinks)
else:
    filename = "test2_{}links".format(xLinks)

#Using the old coefficient array, but it's functionally the same here.
coeff = [[0xb7506a, 0x0, 0x8910c0],
[0xad5074, 0x0, 0x8110c0],
[0xba506e, 0x0, 0x8c10c0],
[0xde6065, 0x0, 0xa620bf],
[0xf56071, 0xf5509c, 0xb820c0],
[0xa15068, 0x0, 0xf220c0],
[0xd05070, 0x0, 0x9c10c0],
[0xe85075, 0xe8409e, 0xae10c1],
[0xc15065, 0x0, 0x9010bf],
[0xba5061, 0xba4094, 0x8b10bf],
[0xf25079, 0x0, 0xb610c1],
[0xb5506f, 0x0, 0x8810c0],
[0xd2606f, 0x0, 0x9d20c0],
[0xb7506f, 0x0, 0x8910c0],
[0x92506c, 0x0, 0xdb20c0],
[0xdf6076, 0x0, 0xa720c1],
[0xe5606e, 0x0, 0xab20c0],
[0x9d5076, 0x0, 0xeb20c1],
[0xfe6061, 0x0, 0xbf20bf],
[0x9a6054, 0x0, 0xe730be],
[0xc26066, 0x0, 0x9220bf],
[0xc06064, 0x0, 0x9020bf],
[0xb45066, 0x0, 0x8710bf],
[0xb1506b, 0x0, 0x8410c0],
[0x8c5077, 0x0, 0xd220c1],
[0x9d5070, 0x0, 0xeb20c0],
[0xcb6059, 0x0, 0x9820be],
[0xc36067, 0x0, 0x9320bf],
[0xae5066, 0x0, 0x8310bf],
[0xcf506f, 0x0, 0x9c10c0],
[0xad5062, 0x0, 0x8210bf],
[0x835069, 0x0, 0xc420c0],
[0x86504e, 0x0, 0xc920bd],
[0x855067, 0x0, 0xc820bf],
[0xdf606b, 0x0, 0xa720c0],
[0xd06070, 0x0, 0x9c20c0],
[0xad505e, 0x0, 0x8210bf],
[0xac5072, 0x0, 0x8110c0],
[0xc5506d, 0x0, 0x9410c0],
[0xbe5063, 0x0, 0x8f10bf],
[0xe9607d, 0x0, 0xaf20c1],
[0x855071, 0x0, 0xc820c0],
[0x9e5077, 0x0, 0xed20c1],
[0xbf5065, 0x0, 0x8f10bf],
[0xe8607a, 0x0, 0xae20c1],
[0xd75071, 0x0, 0xa110c0],
[0x8b506d, 0x0, 0xd020c0],
[0xe06072, 0x0, 0xa820c0]]


N_CHANNEL_IN = 48

class registers:
    
    def __init__(self):
        self.shift_reg = [0,0,0,0]
        self.peak_reg = [0,0] 


def TPG(data_int, lincoeff, r):
  correctedADC = 0
  uncorrectedADC = 0
  linearizerOutput = 0
  base = 0
  coeff = 0
  shiftlin = 0
  mult = 0
  prod = 0
  filterOutput = 0
  shiftfilter = 6
  m = 0
  mul = 0
  pro = 0
  acc = 0
  weight = [24, 31, 16, -35, -36]
  ampPeak = 0
  tmpPeak = 0
  uncorrectedADC = data_int & 0XFFF
  if (((lincoeff & 0XFF0000) >> 16) == 0): coeff = 0
  else: coeff = lincoeff
  base = coeff & 0XFFF
  shiftlin = (coeff & 0XF000) >> 12
  mult = (coeff & 0XFF0000) >> 16 
  correctedADC = (uncorrectedADC - base) 
  if (correctedADC < 0): linearizerOutput = shiftlin << 12 
  prod = correctedADC * mult 
  linearizerOutput = prod >> (shiftlin + 2)
  if (linearizerOutput > 0X30000): linearizerOutput = 0


  m = r.shift_reg[3]
  r.shift_reg[3] = r.shift_reg[2]
  r.shift_reg[2] = r.shift_reg[1]
  r.shift_reg[1] = r.shift_reg[0]
  r.shift_reg[0] = linearizerOutput
  pro = m*weight[4]
  mul = pro >> shiftfilter
  acc = acc + mul
  pro = r.shift_reg[3]*weight[3]
  mul = pro >> shiftfilter
  acc = acc + mul
  pro = r.shift_reg[2]*weight[2]
  mul = pro >> shiftfilter
  acc = acc + mul
  pro = r.shift_reg[1]*weight[1]
  mul = pro >> shiftfilter
  acc = acc + mul
  pro = r.shift_reg[0]*weight[0]
  mul = pro >> shiftfilter
  acc = acc + mul
  filterOutput = acc
  
  if (filterOutput < 0): filterOutput = 0
  if (r.shift_reg[3]==0): filterOutput = 0
  if (filterOutput > 0X3FFFF): filterOutput = 0X3FFFF

  if (r.peak_reg[0] > filterOutput and r.peak_reg[0] > r.peak_reg[1]): 
     ampPeak = r.peak_reg[0]
     if (ampPeak > 0XFFF):
         ampPeak = 0XFFF
  tmpPeak = ampPeak >> 2
  if (tmpPeak > 0X3FF):
         tmpPeak = 0X3FF
         
  r.peak_reg[1] = r.peak_reg[0]
  r.peak_reg[0] = filterOutput
  return "{0:#0{1}x}".format(tmpPeak,6)[2:]

#Writes both the output but also the registers at each stage of input
outFile = open("{0}_out_ref.txt".format(filename),"w")
outFile.write("===================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================== \nWordCnt             LINK_00               LINK_01               LINK_02               LINK_03               LINK_04               LINK_05               LINK_06               LINK_07               LINK_08               LINK_09               LINK_10               LINK_11               LINK_12               LINK_13               LINK_14               LINK_15               LINK_16               LINK_17               LINK_18               LINK_19               LINK_20               LINK_21               LINK_22               LINK_23               LINK_24               LINK_25               LINK_26               LINK_27               LINK_28               LINK_29               LINK_30               LINK_31               LINK_32               LINK_33               LINK_34               LINK_35               LINK_36               LINK_37               LINK_38               LINK_39               LINK_40               LINK_41               LINK_42               LINK_43               LINK_44               LINK_45               LINK_46               LINK_47 \n#BeginData\n")
outFileTwo = open("python_reg_out_{}links.txt".format(xLinks),"w")

mycoeff = 0

with open(filename+"_inp.txt") as inFile:
    #reg only 1D here since the program ignores the zero input crystals, which is every crystal on a link except the 2nd
    reg = [registers() for x in range(xLinks)]
    wrdCnt = 0
    countr = 0
    
    for k,lineOne in enumerate(inFile):
        if k < 3:
            continue

        elif ( wrdCnt % 3 == 0 ):
            link_out = ["00000000"]*xLinks
            lineArray = re.split(r'[ \n]', lineOne)
            tmpLinkAr = [x for x in lineArray[1:] if x !=""]
            
            for lnk,tpLink in enumerate(tmpLinkAr[:xLinks]):
                link_in = "0x00000000000000000000000000000000"+tpLink[2:]
                j = int(link_in[38])
                mycoeff = coeff[lnk][j-1]
                link_out[lnk] = '000000000000000000000000000000000000'+TPG(int(link_in[38:42],16), mycoeff, reg[lnk])+link_out[lnk]
                
            outFileTwo.write("start "+str(countr)+"\n")
            print("shift "+str(reg[0].shift_reg[0])+" "+str(reg[0].shift_reg[1])+" "+str(reg[0].shift_reg[2])+" "+str(reg[0].shift_reg[3]))
            print("peak "+str(reg[0].peak_reg[0])+" "+str(reg[0].peak_reg[1]))
            
            for l in range(xLinks):
                outFileTwo.write("shift "+str(l)+" "+str(reg[l].shift_reg[0])+" "+str(reg[l].shift_reg[1])+" "+str(reg[l].shift_reg[2])+" "+str(reg[l].shift_reg[3])+"\n")
                outFileTwo.write("peak "+str(l)+" "+str(reg[l].peak_reg[0])+" "+str(reg[l].peak_reg[1])+"\n")
                outFileTwo.write("next"+"\n")
    
            countr += 1
            
            for cyc in range(3):
                outFile.write("{0:#0{1}x}   ".format(wrdCnt+cyc,6))
                for lnk in range(0,xLinks):
                    outFile.write("0x"+"{0}".format(link_out[lnk][32-(cyc*16):48-(cyc*16)])+"    ")
                for lnk in range(xLinks,N_CHANNEL_IN):
                        outFile.write("0x0000000000000000"+"    ")
                outFile.write("\n")
        wrdCnt+=1
            
outFile.close()
outFileTwo.close()