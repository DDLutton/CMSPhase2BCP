#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 11:32:21 2019

@author: lutton
"""

#This makes random coefficients
#Probably not really important, particularly since having run it once on 48 links gives an array that works.
#but it's here if you want it.

import numpy as np

#For a minute I thought I needed a 1D array instead of a 2D array, so this option makes that.
oneD = False

xLinks = 2
NCrystalsPerLink = 11

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

prob1stAr = [[[8, 0.125],
  [9, 0.10416666666666667],
  [10, 0.125],
  [11, 0.1875],
  [12, 0.14583333333333334],
  [13, 0.14583333333333334],
  [14, 0.10416666666666667],
  [15, 0.0625]],
 [[5, 0.020833333333333332],
  [6, 0.0625],
  [21, 0.0625],
  [37, 0.041666666666666664],
  [38, 0.041666666666666664],
  [53, 0.020833333333333332],
  [54, 0.020833333333333332],
  [69, 0.020833333333333332],
  [85, 0.08333333333333333],
  [86, 0.041666666666666664],
  [101, 0.020833333333333332],
  [117, 0.0625],
  [133, 0.020833333333333332],
  [134, 0.020833333333333332],
  [150, 0.020833333333333332],
  [165, 0.041666666666666664],
  [166, 0.020833333333333332],
  [181, 0.020833333333333332],
  [182, 0.020833333333333332],
  [197, 0.041666666666666664],
  [213, 0.10416666666666667],
  [229, 0.0625],
  [230, 0.041666666666666664],
  [245, 0.041666666666666664],
  [246, 0.041666666666666664]],
 [[78, 0.020833333333333332],
  [84, 0.020833333333333332],
  [89, 0.020833333333333332],
  [94, 0.020833333333333332],
  [97, 0.041666666666666664],
  [98, 0.020833333333333332],
  [99, 0.020833333333333332],
  [100, 0.020833333333333332],
  [101, 0.0625],
  [102, 0.0625],
  [103, 0.041666666666666664],
  [104, 0.020833333333333332],
  [105, 0.020833333333333332],
  [106, 0.020833333333333332],
  [107, 0.041666666666666664],
  [108, 0.020833333333333332],
  [109, 0.041666666666666664],
  [110, 0.041666666666666664],
  [111, 0.08333333333333333],
  [112, 0.0625],
  [113, 0.0625],
  [114, 0.041666666666666664],
  [116, 0.020833333333333332],
  [117, 0.020833333333333332],
  [118, 0.041666666666666664],
  [119, 0.041666666666666664],
  [121, 0.020833333333333332],
  [122, 0.020833333333333332],
  [125, 0.020833333333333332]]]

prob2ndAr = [[[11, 11, 0.3333333333333333],
  [14, 14, 0.3333333333333333],
  [15, 15, 0.3333333333333333]],
 [[86, 85, 0.3333333333333333],
  [133, 132, 0.3333333333333333],
  [165, 164, 0.3333333333333333]],
 [[97, 148, 0.3333333333333333],
  [113, 156, 0.3333333333333333],
  [117, 158, 0.3333333333333333]]]

prob3rdAr = [[[8, None, 12, 0.6666666666666666],
  [8, None, 13, 0.3333333333333333],
  [9, None, 13, 0.2],
  [9, None, 14, 0.8],
  [10, None, 8, 0.8333333333333334],
  [10, None, 15, 0.16666666666666666],
  [11, None, 8, 1.0],
  [11, 11, 8, 1.0],
  [12, None, 9, 1.0],
  [13, None, 9, 0.42857142857142855],
  [13, None, 10, 0.5714285714285714],
  [14, None, 10, 1.0],
  [14, 14, 10, 1.0],
  [15, None, 11, 1.0],
  [15, 15, 11, 1.0]],
 [[5, None, 193, 1.0],
  [6, None, 2, 0.3333333333333333],
  [6, None, 130, 0.3333333333333333],
  [6, None, 194, 0.3333333333333333],
  [21, None, 1, 0.3333333333333333],
  [21, None, 34, 0.3333333333333333],
  [21, None, 65, 0.3333333333333333],
  [37, None, 97, 0.5],
  [37, None, 178, 0.5],
  [38, None, 34, 0.5],
  [38, None, 210, 0.5],
  [53, None, 66, 1.0],
  [54, None, 50, 1.0],
  [69, None, 113, 1.0],
  [85, None, 65, 0.25],
  [85, None, 129, 0.25],
  [85, None, 130, 0.5],
  [86, None, 178, 1.0],
  [86, 85, 130, 1.0],
  [101, None, 146, 1.0],
  [117, None, 17, 0.3333333333333333],
  [117, None, 145, 0.6666666666666666],
  [133, 132, 225, 1.0],
  [134, None, 226, 1.0],
  [150, None, 242, 1.0],
  [165, None, 193, 1.0],
  [165, 164, 177, 1.0],
  [166, None, 115, 1.0],
  [181, None, 2, 1.0],
  [182, None, 130, 1.0],
  [197, None, 17, 0.5],
  [197, None, 34, 0.5],
  [213, None, 17, 0.2],
  [213, None, 33, 0.4],
  [213, None, 178, 0.4],
  [229, None, 49, 0.3333333333333333],
  [229, None, 210, 0.3333333333333333],
  [229, None, 241, 0.3333333333333333],
  [230, None, 98, 0.5],
  [230, None, 242, 0.5],
  [245, None, 193, 0.5],
  [245, None, 241, 0.5],
  [246, None, 114, 1.0]],
 [[78, None, 189, 1.0],
  [84, None, 190, 1.0],
  [89, None, 190, 1.0],
  [94, None, 191, 1.0],
  [97, None, 191, 1.0],
  [97, 148, 191, 1.0],
  [98, None, 191, 1.0],
  [99, None, 191, 1.0],
  [100, None, 191, 1.0],
  [101, None, 191, 1.0],
  [102, None, 191, 1.0],
  [103, None, 191, 1.0],
  [104, None, 192, 1.0],
  [105, None, 192, 1.0],
  [106, None, 192, 1.0],
  [107, None, 192, 1.0],
  [108, None, 192, 1.0],
  [109, None, 192, 1.0],
  [110, None, 192, 1.0],
  [111, None, 192, 1.0],
  [112, None, 192, 1.0],
  [113, None, 192, 1.0],
  [113, 156, 192, 1.0],
  [114, None, 192, 1.0],
  [116, None, 192, 1.0],
  [117, 158, 193, 1.0],
  [118, None, 193, 1.0],
  [119, None, 193, 1.0],
  [121, None, 193, 1.0],
  [122, None, 193, 1.0],
  [125, None, 193, 1.0]]]

prob4thAr = [[[8, 12, 0.6666666666666666],
  [8, 13, 0.3333333333333333],
  [9, 13, 0.2],
  [9, 14, 0.8],
  [10, 8, 0.8333333333333334],
  [10, 15, 0.16666666666666666],
  [11, 8, 1.0],
  [12, 9, 1.0],
  [13, 9, 0.42857142857142855],
  [13, 10, 0.5714285714285714],
  [14, 10, 1.0],
  [15, 11, 1.0]],
 [[5, 193, 1.0],
  [6, 2, 0.3333333333333333],
  [6, 130, 0.3333333333333333],
  [6, 194, 0.3333333333333333],
  [21, 1, 0.3333333333333333],
  [21, 34, 0.3333333333333333],
  [21, 65, 0.3333333333333333],
  [37, 97, 0.5],
  [37, 178, 0.5],
  [38, 34, 0.5],
  [38, 210, 0.5],
  [53, 66, 1.0],
  [54, 50, 1.0],
  [69, 113, 1.0],
  [85, 65, 0.25],
  [85, 129, 0.25],
  [85, 130, 0.5],
  [86, 178, 0.5],
  [86, 130, 0.5],
  [101, 146, 1.0],
  [117, 17, 0.3333333333333333],
  [117, 145, 0.6666666666666666],
  [133, 225, 1.0],
  [134, 226, 1.0],
  [150, 242, 1.0],
  [165, 193, 0.5],
  [165, 177, 0.5],
  [166, 115, 1.0],
  [181, 2, 1.0],
  [182, 130, 1.0],
  [197, 17, 0.5],
  [197, 34, 0.5],
  [213, 17, 0.2],
  [213, 33, 0.4],
  [213, 178, 0.4],
  [229, 49, 0.3333333333333333],
  [229, 210, 0.3333333333333333],
  [229, 241, 0.3333333333333333],
  [230, 98, 0.5],
  [230, 242, 0.5],
  [245, 193, 0.5],
  [245, 241, 0.5],
  [246, 114, 1.0]],
 [[78, 189, 1.0],
  [84, 190, 1.0],
  [89, 190, 1.0],
  [94, 191, 1.0],
  [97, 191, 1.0],
  [98, 191, 1.0],
  [99, 191, 1.0],
  [100, 191, 1.0],
  [101, 191, 1.0],
  [102, 191, 1.0],
  [103, 191, 1.0],
  [104, 192, 1.0],
  [105, 192, 1.0],
  [106, 192, 1.0],
  [107, 192, 1.0],
  [108, 192, 1.0],
  [109, 192, 1.0],
  [110, 192, 1.0],
  [111, 192, 1.0],
  [112, 192, 1.0],
  [113, 192, 1.0],
  [114, 192, 1.0],
  [116, 192, 1.0],
  [117, 193, 1.0],
  [118, 193, 1.0],
  [119, 193, 1.0],
  [121, 193, 1.0],
  [122, 193, 1.0],
  [125, 193, 1.0]]]
 
prob1stArNP = np.array([np.array([np.array(x) for x in y]) for y in prob1stAr])
prob2ndArNP = np.array([np.array([np.array(x) for x in y]) for y in prob2ndAr])
prob3rdArNP = np.array([np.array([np.array(x) for x in y]) for y in prob3rdAr])
prob4thArNP = np.array([np.array([np.array(x) for x in y]) for y in prob4thAr])


minNames = ["minlF","minnE","minfT"]
maxNames = ["maxlF","maxnE","maxfT"]
minmaxDict = {}

for i in range(3):
    minmaxDict[minNames[i]] = min(min(prob3rdArNP[i][np.where((prob3rdArNP[i])[:,2] != None),2][0]),min(min(prob3rdArNP[i][np.where((prob3rdArNP[i])[:,1] != None),1][0]),min(prob3rdArNP[i][np.where((prob3rdArNP[i])[:,0] != None),0][0])))
    minmaxDict[maxNames[i]] = max(max(prob3rdArNP[i][np.where((prob3rdArNP[i])[:,2] != None),2][0]),max(max(prob3rdArNP[i][np.where((prob3rdArNP[i])[:,1] != None),1][0]),max(prob3rdArNP[i][np.where((prob3rdArNP[i])[:,0] != None),0][0])))

    
 
def con1stCo():
    lF = int(np.random.choice(prob1stArNP[0][:,0],p=prob1stArNP[0][:,1]))
    nE = int(np.random.choice(prob1stArNP[1][:,0],p=prob1stArNP[1][:,1]))
    fT = int(np.random.choice(prob1stArNP[2][:,0],p=prob1stArNP[2][:,1]))
    return [lF,nE,fT]#change to 

def con2ndCo(coOne):
    
    lF = coOne[0]
    nE = coOne[1]-1
    if nE < minmaxDict[minNames[1]]:
        nE = minmaxDict[minNames[1]]
    elif nE > minmaxDict[maxNames[1]]:
        nE = minmaxDict[minNames[1]]
    fT = coOne[2]+51-((coOne[2]-97)//2)
    if fT < minmaxDict[minNames[2]]:
        fT = minmaxDict[minNames[2]]
    elif fT > minmaxDict[maxNames[2]]:
        fT = minmaxDict[minNames[2]]
    return [lF,nE,fT]
    
def con3rdCo(coOne):
    tmpAr = np.array([ar[1:] for ar in prob4thArNP[0] if ar[0]==coOne[0]])
    lF = int(np.random.choice(tmpAr[:,0],p=tmpAr[:,1]))
    tmpAr = np.array([ar[1:] for ar in prob4thArNP[1] if ar[0]==coOne[1]])
    nE = int(np.random.choice(tmpAr[:,0],p=tmpAr[:,1]))
    tmpAr = np.array([ar[1:] for ar in prob4thArNP[2] if ar[0]==coOne[2]])
    fT = int(np.random.choice(tmpAr[:,0],p=tmpAr[:,1]))
    return [lF,nE,fT]

coeffAr= np.zeros([xLinks*NCrystalsPerLink, 3],dtype=int)
impLinks = [(NCrystalsPerLink*i)+1 for i in range(xLinks)]
iLCount = 0
doneLinks = [4,7,9]

for i in range(xLinks*NCrystalsPerLink):
    if i in impLinks:
        
        if iLCount in doneLinks:
            coeffAr[i] = coeff[iLCount]
        else:
            tmpA = [int('{0:024b}'.format(coeff[iLCount][0])[:4],2),int('{0:024b}'.format(coeff[iLCount][0])[4:12],2),int('{0:024b}'.format(coeff[iLCount][0])[12:24],2)]
            tmpB = con2ndCo(tmpA)
            coeffAr[i] = [coeff[iLCount][0],int('{0:04b}'.format(tmpB[0])+'{0:08b}'.format(tmpB[1])+'{0:012b}'.format(tmpB[2]),2),coeff[iLCount][2]]
        iLCount += 1
    else:
        tmpA = con1stCo()
        tmpB = con2ndCo(tmpA)
        tmpC = con3rdCo(tmpA)
        coeffAr[i] = [int('{0:04b}'.format(tmpA[0])+'{0:08b}'.format(tmpA[1])+'{0:012b}'.format(tmpA[2]),2),int('{0:04b}'.format(tmpB[0])+'{0:08b}'.format(tmpB[1])+'{0:012b}'.format(tmpB[2]),2),int('{0:04b}'.format(tmpC[0])+'{0:08b}'.format(tmpC[1])+'{0:012b}'.format(tmpC[2]),2)]

if oneD:
    outFile = open("{0}links{1}crystals_Gen_coeffArrays_OneD.txt".format(xLinks,NCrystalsPerLink),"w")
    outFile.write("C coeff:\n")
    outFile.write("static const uint24_t coeff[{0}] = {{".format(xLinks*NCrystalsPerLink*3)+hex(coeffAr[0][0])+", "+hex(coeffAr[0][1])+", "+hex(coeffAr[0][2]))
    for ar in coeffAr[1:]:
        outFile.write(", "+hex(ar[0]))
        for element in ar[1:]:
            outFile.write(", "+hex(element))
    outFile.write("};\n")
            
    outFile.write("Python coeff:\n")
    outFile.write("coeff = ["+hex(coeffAr[0][0])+", "+hex(coeffAr[0][1])+", "+hex(coeffAr[0][2]))
    for ar in coeffAr[1:]:
        outFile.write(", "+hex(ar[0]))
        for element in ar[1:]:
            outFile.write(", "+hex(element))
    outFile.write("]\n")

else:
    outFile = open("{0}links{1}crystals_Gen_coeffArrays.txt".format(xLinks,NCrystalsPerLink),"w")
    outFile.write("C coeff:\n")
    outFile.write("static const uint24_t coeff[{0}][3] = {{{{".format(xLinks*NCrystalsPerLink)+hex(coeffAr[0][0])+", "+hex(coeffAr[0][1])+", "+hex(coeffAr[0][2])+"}")
    for ar in coeffAr[1:]:
        outFile.write(",\n{"+hex(ar[0]))
        for element in ar[1:]:
            outFile.write(", "+hex(element))
        outFile.write("}")
    outFile.write("};\n")
            
    outFile.write("Python coeff:\n")
    outFile.write("coeff = [["+hex(coeffAr[0][0])+", "+hex(coeffAr[0][1])+", "+hex(coeffAr[0][2])+"]")
    for ar in coeffAr[1:]:
        outFile.write(",\n["+hex(ar[0]))
        for element in ar[1:]:
            outFile.write(", "+hex(element))
        outFile.write("]")
    outFile.write("]\n")

outFile.close()
