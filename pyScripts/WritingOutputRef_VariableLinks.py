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
addGain = False

#For new multiEvent files
multiEvent = True
xEvents = 8
NCrystalsPerLink = 11
maxCrystals = 300

#If the registers are initialized by a fake event of repeated input:
initEvent = True
initAllEvents = True

#Only output the registers from one crystal for testing
outOneCrystal = True
if outOneCrystal:
    wrdCntForCry = 2
    lnkForCry = 0
    cryOnLnk=7

if addGain:
    if multiEvent or initEvent:
        print("not yet imp")
    else:
        filename = "test2_{}links_AddedGain".format(xLinks)
else:
    if multiEvent:
        if initEvent:
            if initAllEvents:
                filename = "test2_100Events_300Channels__{}evts_{}links_IAE".format(xEvents,xLinks)
            else:
                filename = "test2_100Events_300Channels__{}evts_{}links_IE".format(xEvents,xLinks)
        else:
            filename = "test2_100Events_300Channels__{}evts_{}links".format(xEvents,xLinks)

    else:
        if initEvent:
            print("not yet imp")
        else:
            filename = "test2_{}links".format(xLinks)
if multiEvent:
    coeff = [[0xad6066, 0xad5097, 0x8220bf],
[0xc26062, 0xc25095, 0x9220bf],
[0xb1605c, 0xb15092, 0x8420bf],
[0xd46074, 0xd4509e, 0x9d20c0],
[0xa86064, 0xa85096, 0x8120bf],
[0xa46062, 0xa45095, 0xf220bf],
[0xb26070, 0xb2509c, 0x8420c0],
[0xaa6067, 0xaa5097, 0x8120bf],
[0xce6079, 0xce50a0, 0x9c20c1],
[0xb56060, 0xb55094, 0x8820bf],
[0xb2606b, 0xb25099, 0x8420c0],
[0xad6064, 0xad5096, 0x8220bf],
[0xad606e, 0xad509b, 0x8120c0],
[0xb3605c, 0xb35092, 0x8720bf],
[0xb9606f, 0xb9509b, 0x8c20c0],
[0xb06071, 0xb0509c, 0x8420c0],
[0xae605d, 0xae5092, 0x8320bf],
[0xb36069, 0xb35098, 0x8720c0],
[0xa06057, 0xa0508f, 0xf220be],
[0xa76061, 0xa75094, 0x8120bf],
[0xb36069, 0xb35098, 0x8720c0],
[0xad6066, 0xad5097, 0x8220bf],
[0xae6061, 0xae5094, 0x8320bf],
[0xad6068, 0xad5098, 0x8120c0],
[0xa9605b, 0xa95091, 0x8120be],
[0xb86071, 0xb8509c, 0x8920c0],
[0xa16057, 0xa1508f, 0xf220be],
[0xb2606a, 0xb25099, 0x8420c0],
[0xc3606f, 0xc3509b, 0x9320c0],
[0xaa6056, 0xaa508f, 0x8120be],
[0xad6068, 0xad5098, 0x8220c0],
[0xa66063, 0xa65095, 0xf220bf],
[0xaa605b, 0xaa5091, 0x8120be],
[0xa46064, 0xa45096, 0xf220bf],
[0xb1605d, 0xb15092, 0x8420bf],
[0xba606d, 0xba509a, 0x8b20c0],
[0xa76067, 0xa75097, 0x8120bf],
[0xac6059, 0xac5090, 0x8120be],
[0xa86061, 0xa85094, 0x8120bf],
[0xb56065, 0xb55096, 0x8820bf],
[0xb0606c, 0xb0509a, 0x8420c0],
[0xa1605e, 0xa15093, 0xf220bf],
[0x9c6051, 0x9c508c, 0xeb20be],
[0xac6065, 0xac5096, 0x8120bf],
[0xb06062, 0xb05095, 0x8420bf],
[0xb0606e, 0xb0509b, 0x8420c0],
[0xb56065, 0xb55096, 0x8820bf],
[0xa16063, 0xa15095, 0xf220bf],
[0xaf6060, 0xaf5094, 0x8320bf],
[0xae6072, 0xae509d, 0x8320c0],
[0xa4605f, 0xa45093, 0xf220bf],
[0xb1605c, 0xb15092, 0x8430bf],
[0xb0605c, 0xb05092, 0x8420bf],
[0xb06066, 0xb05097, 0x8420bf],
[0xa46065, 0xa45096, 0xf220bf],
[0xaa605b, 0xaa5091, 0x8120be],
[0xab606b, 0xab5099, 0x8120c0],
[0xab6061, 0xab5094, 0x8120bf],
[0xa16066, 0xa15097, 0xf220bf],
[0xa16060, 0xa15094, 0xf220bf],
[0xb36064, 0xb35096, 0x8720bf],
[0x9e6065, 0x9e5096, 0xed30bf],
[0xaa606b, 0xaa5099, 0x8120c0],
[0xa8605b, 0xa85091, 0x8120be],
[0xb36072, 0xb3509d, 0x8720c0],
[0xa06065, 0xa05096, 0xf220bf],
[0xa16059, 0xa15090, 0xf220be],
[0xa16068, 0xa15098, 0xf220c0],
[0xa86067, 0xa85097, 0x8120bf],
[0xa1605f, 0xa15093, 0xf220bf],
[0xa96060, 0xa95094, 0x8120bf],
[0xaa605d, 0xaa5092, 0x8120bf],
[0xaa605f, 0xaa5093, 0x8120bf],
[0xb06064, 0xb05096, 0x8420bf],
[0xab6059, 0xab5090, 0x8120be],
[0xb0606a, 0xb05099, 0x8430c0],
[0xb0606d, 0xb0509a, 0x8420c0],
[0xad6054, 0xad508e, 0x8220be],
[0xb16063, 0xb15095, 0x8420bf],
[0xb16064, 0xb15096, 0x8420bf],
[0xb66064, 0xb65096, 0x8920bf],
[0xb1605c, 0xb15092, 0x8420bf],
[0xb36062, 0xb35095, 0x8720bf],
[0xaf6060, 0xaf5094, 0x8320bf],
[0xa76064, 0xa75096, 0x8120bf],
[0xa76068, 0xa75098, 0x8120c0],
[0xaa6064, 0xaa5096, 0x8120bf],
[0xa36061, 0xa35094, 0xf220bf],
[0xad6069, 0xad5098, 0x8220c0],
[0xaf6069, 0xaf5098, 0x8320c0],
[0xa46066, 0xa45097, 0xf220bf],
[0xaf605d, 0xaf5092, 0x8320bf],
[0xa4605b, 0xa45091, 0xf220be],
[0xa46055, 0xa4508e, 0xf220be],
[0xa86067, 0xa85097, 0x8130bf],
[0xa86062, 0xa85095, 0x8120bf],
[0xa66063, 0xa65095, 0xf220bf],
[0xa7605c, 0xa75092, 0x8120bf],
[0xa8606d, 0xa8509a, 0x8120c0],
[0xaf605f, 0xaf5093, 0x8320bf],
[0x9e604e, 0x9e508b, 0xed20bd],
[0xae6066, 0xae5097, 0x8320bf],
[0xac6060, 0xac5094, 0x8120bf],
[0xc16075, 0xc1509e, 0x9020c1],
[0xa96062, 0xa95095, 0x8120bf],
[0xb06067, 0xb05097, 0x8420bf],
[0xac6069, 0xac5098, 0x8120c0],
[0xa76067, 0xa75097, 0x8120bf],
[0xb56069, 0xb55098, 0x8820c0],
[0x9e6056, 0x9e508f, 0xed20be],
[0xb46067, 0xb45097, 0x8720bf],
[0xa66056, 0xa6508f, 0xf230be],
[0x99604f, 0x99508b, 0xe720bd],
[0xb26059, 0xb25090, 0x8420be],
[0xae6064, 0xae5096, 0x8320bf],
[0xa96056, 0xa9508f, 0x8120be],
[0xb3606d, 0xb3509a, 0x8720c0],
[0x9c604e, 0x9c508b, 0xeb20bd],
[0xa8605e, 0xa85093, 0x8120bf],
[0xa66062, 0xa65095, 0xf220bf],
[0xac6061, 0xac5094, 0x8120bf],
[0xa5605a, 0xa55091, 0xf220be],
[0xa16060, 0xa15094, 0xf220bf],
[0xae605c, 0xae5092, 0x8320bf],
[0xa16062, 0xa15095, 0xf220bf],
[0xad6067, 0xad5097, 0x8120bf],
[0xa8605e, 0xa85093, 0x8120bf],
[0xa56059, 0xa55090, 0xf220be],
[0xa56059, 0xa55090, 0xf220be],
[0xab6058, 0xab5090, 0x8120be],
[0xa9605a, 0xa95091, 0x8120be],
[0xa2605c, 0xa25092, 0xf220bf],
[0xaf6066, 0xaf5097, 0x8320bf],
[0xa66054, 0xa6508e, 0xf230be],
[0xa96061, 0xa95094, 0x8120bf],
[0xa36066, 0xa35097, 0xf220bf],
[0xac606f, 0xac509b, 0x8120c0],
[0xa4605d, 0xa45092, 0xf220bf],
[0xa4605e, 0xa45093, 0xf220bf],
[0xa0605f, 0xa05093, 0xf220bf],
[0xa36066, 0xa35097, 0xf220bf],
[0x9d6060, 0x9d5094, 0xeb20bf],
[0xa66065, 0xa65096, 0xf230bf],
[0x92604a, 0x925089, 0xdb20bd],
[0xad6068, 0xad5098, 0x8230c0],
[0xa56065, 0xa55096, 0xf220bf],
[0x9b605b, 0x9b5091, 0xe720be],
[0xa8605c, 0xa85092, 0x8120bf],
[0x93605d, 0x935092, 0xdb20bf],
[0xa46064, 0xa45096, 0xf220bf],
[0x9d604d, 0x9d508a, 0xeb20bd],
[0xac605a, 0xac5091, 0x8120be],
[0x956044, 0x955086, 0xdb20bd],
[0x9b605a, 0x9b5091, 0xe720be],
[0xa7605e, 0xa75093, 0x8120bf],
[0x9a604f, 0x9a508b, 0xe720bd],
[0xa26058, 0xa25090, 0xf220be],
[0xa56055, 0xa5508e, 0xf230be],
[0x956049, 0x955088, 0xdb30bd],
[0x9a6057, 0x9a508f, 0xe720be],
[0xa46063, 0xa45095, 0xf220bf],
[0x9b6059, 0x9b5090, 0xe720be],
[0xa76066, 0xa75097, 0x8120bf],
[0xa06065, 0xa05096, 0xf220bf],
[0xa66061, 0xa65094, 0xf220bf],
[0x98605f, 0x985093, 0xe720bf],
[0x9e6055, 0x9e508e, 0xed20be],
[0xa0605a, 0xa05091, 0xf220be],
[0xa06058, 0xa05090, 0xf220be],
[0x9e6057, 0x9e508f, 0xed20be],
[0xa56060, 0xa55094, 0xf220bf],
[0x96604d, 0x96508a, 0xe720bd],
[0x9b6063, 0x9b5095, 0xe720bf],
[0x8f6053, 0x8f508d, 0xdb20be],
[0x92604f, 0x92508b, 0xdb20bd],
[0xaa6058, 0xaa5090, 0x8120be],
[0x976049, 0x975088, 0xe720bd],
[0xa6605c, 0xa65092, 0xf220bf],
[0xa2605d, 0xa25092, 0xf220bf],
[0x956056, 0x95508f, 0xdb20be],
[0xa7605d, 0xa75092, 0x8120bf],
[0xa5605e, 0xa55093, 0xf220bf],
[0x9e605f, 0x9e5093, 0xed20bf],
[0x9f6063, 0x9f5095, 0xed20bf],
[0x956052, 0x95508d, 0xdb20be],
[0xb3606b, 0xb35099, 0x8720c0],
[0xa7605c, 0xa75092, 0x8120bf],
[0x9a6055, 0x9a508e, 0xe720be],
[0xa06053, 0xa0508d, 0xf220be],
[0x9b605b, 0x9b5091, 0xe720be],
[0x966056, 0x96508f, 0xe720be],
[0x9d6058, 0x9d5090, 0xeb20be],
[0x9f6055, 0x9f508e, 0xed20be],
[0x9d6058, 0x9d5090, 0xeb20be],
[0xa0605b, 0xa05091, 0xf220be],
[0x9c6053, 0x9c508d, 0xeb20be],
[0x9d605e, 0x9d5093, 0xeb20bf],
[0x91605d, 0x915092, 0xdb20bf],
[0x9e6063, 0x9e5095, 0xed20bf],
[0xa26065, 0xa25096, 0xf220bf],
[0xd06076, 0xd0509f, 0x9c20c1],
[0xa56059, 0xa55090, 0xf220be],
[0xbf6065, 0xbf5096, 0x8f20bf],
[0xc56070, 0xc5509c, 0x9420c0],
[0xcf6073, 0xcf509d, 0x9c20c0],
[0xce6069, 0xce5098, 0x9c20c0],
[0x9c6058, 0x9c5090, 0xeb20be],
[0xc2606d, 0xc2509a, 0x9220c0],
[0xb2605e, 0xb25093, 0x8420bf],
[0xb16066, 0xb15097, 0x8420bf],
[0xad605a, 0xad5091, 0x8220be],
[0xa76068, 0xa75098, 0x8130c0],
[0xab606c, 0xab509a, 0x8130c0],
[0xb6606a, 0xb65099, 0x8920c0],
[0xb5605e, 0xb55093, 0x8820bf],
[0xb86077, 0xb8509f, 0x8920c1],
[0x9c6051, 0x9c508c, 0xeb20be],
[0xc56066, 0xc55097, 0x9420bf],
[0x936055, 0x93508e, 0xdb20be],
[0xa66059, 0xa65090, 0xf220be],
[0xbe6075, 0xbe509e, 0x8f20c1],
[0x98604f, 0x98508b, 0xe720bd],
[0xbd6070, 0xbd509c, 0x8f20c0],
[0xa26056, 0xa2508f, 0xf220be],
[0x92605d, 0x925092, 0xdb30bf],
[0xa16056, 0xa1508f, 0xf230be],
[0x916046, 0x915087, 0xdb20bd],
[0x9e6061, 0x9e5094, 0xed20bf],
[0xad605f, 0xad5093, 0x8120bf],
[0x9a6056, 0x9a508f, 0xe720be],
[0xa16059, 0xa15090, 0xf220be],
[0x9a605d, 0x9a5092, 0xe720bf],
[0xa9605a, 0xa95091, 0x8120be],
[0x9c6059, 0x9c5090, 0xeb20be],
[0xb26066, 0xb25097, 0x8420bf],
[0x9d604e, 0x9d508b, 0xeb20bd],
[0x99604e, 0x99508b, 0xe720bd],
[0xa16066, 0xa15097, 0xf230bf],
[0x986050, 0x98508c, 0xe720bd],
[0xa46053, 0xa4508d, 0xf220be],
[0xa76056, 0xa7508f, 0x8120be],
[0xa0605e, 0xa05093, 0xf220bf],
[0xaa606b, 0xaa5099, 0x8130c0],
[0x96604d, 0x96508a, 0xe720bd],
[0x936053, 0x93508d, 0xdb20be],
[0xa2605c, 0xa25092, 0xf220bf],
[0x986057, 0x98508f, 0xe720be],
[0x97605f, 0x975093, 0xe720bf],
[0x90604b, 0x905089, 0xdb20bd],
[0x9b605a, 0x9b5091, 0xe720be],
[0x936047, 0x935087, 0xdb20bd],
[0x986052, 0x98508d, 0xe730be],
[0x936055, 0x93508e, 0xdb20be],
[0x966051, 0x96508c, 0xe720be],
[0x966057, 0x96508f, 0xe730be],
[0xa0604e, 0xa0508b, 0xf220bd],
[0x936056, 0x93508f, 0xdb20be],
[0xb96062, 0xb95095, 0x8b20bf],
[0x966053, 0x96508d, 0xe720be],
[0x96604a, 0x965089, 0xe720bd],
[0x936050, 0x93508c, 0xdb20bd],
[0x9d604f, 0x9d508b, 0xeb20bd],
[0x946057, 0x94508f, 0xdb20be],
[0x926046, 0x925087, 0xdb20bd],
[0x996062, 0x995095, 0xe730bf],
[0x94605c, 0x945092, 0xdb20bf],
[0x98605f, 0x985093, 0xe720bf],
[0x8c6047, 0x8c5087, 0xd220bd],
[0x8c6055, 0x8c508e, 0xd220be],
[0x94605c, 0x945092, 0xdb20bf],
[0x956062, 0x955095, 0xdb20bf],
[0x98605e, 0x985093, 0xe720bf],
[0x986054, 0x98508e, 0xe720be],
[0xa76061, 0xa75094, 0x8120bf],
[0x956050, 0x95508c, 0xdb20bd],
[0x956056, 0x95508f, 0xdb20be],
[0x9a6057, 0x9a508f, 0xe720be],
[0xaa605f, 0xaa5093, 0x8120bf],
[0xb26065, 0xb25096, 0x8420bf],
[0x9a604d, 0x9a508a, 0xe720bd],
[0x98605e, 0x985093, 0xe730bf],
[0x8e6050, 0x8e508c, 0xd220bd],
[0x9a605a, 0x9a5091, 0xe720be],
[0x98605e, 0x985093, 0xe720bf],
[0x966055, 0x96508e, 0xe720be],
[0x95604b, 0x955089, 0xdb20bd],
[0x956048, 0x955088, 0xdb20bd],
[0x94605a, 0x945091, 0xdb20be],
[0x976055, 0x97508e, 0xe720be],
[0x916052, 0x91508d, 0xdb20be],
[0x92604f, 0x92508b, 0xdb20bd],
[0xa96068, 0xa95098, 0x8120c0],
[0x8f6049, 0x8f5088, 0xdb20bd],
[0xa06069, 0xa05098, 0xf220c0],
[0x93604e, 0x93508b, 0xdb20bd],
[0x986062, 0x985095, 0xe720bf],
[0xb2606d, 0xb2509a, 0x8420c0],
[0x94604a, 0x945089, 0xdb20bd],
[0x956060, 0x955094, 0xdb20bf],
[0x94604d, 0x94508a, 0xdb20bd]]
else:
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


def TPG(data_int, lincoeff, r,checkProb):
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
  prod = correctedADC * mult 
  linearizerOutput = prod >> (shiftlin + 2)
  if (linearizerOutput > 0X30000 or correctedADC < 0): linearizerOutput = 0
  if checkProb:
      print("chckprob")
      print(str(uncorrectedADC)+" "+str(coeff)+" "+str(base)+" "+str(shiftlin)+" "+str(mult)+" "+str(correctedADC)+" "+str(prod)+" "+str(linearizerOutput))

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
  if checkProb:
      print(filterOutput)
      print(m)
      print(r.shift_reg[3])
      print(r.shift_reg[2])
      print(r.shift_reg[1])
      print(r.shift_reg[0])
  
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
  if checkProb:
      print(ampPeak,tmpPeak)
  return "{0:#0{1}x}".format(tmpPeak,6)[2:]

      
if __name__ == "__main__":
    #Writes both the output but also the registers at each stage of input
    outFile = open("{0}_FromTPG_out_ref.txt".format(filename),"w")
    outFile.write("===================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================== \nWordCnt             LINK_00               LINK_01               LINK_02               LINK_03               LINK_04               LINK_05               LINK_06               LINK_07               LINK_08               LINK_09               LINK_10               LINK_11               LINK_12               LINK_13               LINK_14               LINK_15               LINK_16               LINK_17               LINK_18               LINK_19               LINK_20               LINK_21               LINK_22               LINK_23               LINK_24               LINK_25               LINK_26               LINK_27               LINK_28               LINK_29               LINK_30               LINK_31               LINK_32               LINK_33               LINK_34               LINK_35               LINK_36               LINK_37               LINK_38               LINK_39               LINK_40               LINK_41               LINK_42               LINK_43               LINK_44               LINK_45               LINK_46               LINK_47 \n#BeginData\n")
    if multiEvent:
        outFileTwo = open("python_reg_out_{}evts_{}links.txt".format(xEvents,xLinks),"w")
    else:
        outFileTwo = open("python_reg_out_{}links.txt".format(xLinks),"w")
    
    mycoeff = 0
    
    with open(filename+"_inp.txt") as inFile:
        if multiEvent:
            reg = [[registers() for y in range(NCrystalsPerLink)] for x in range(xLinks)]
        else:
            #reg only 1D here since the program ignores the zero input crystals, which is every crystal on a link except the 2nd
            reg = [registers() for x in range(xLinks)]
        wrdCnt = 0
        countr = 0
        toAdd = 0
        countUp = 0
        checkProb = False
        for k,lineOne in enumerate(inFile):
            if k < 3:
                continue
            #For this I'm going to treat the link_out/link_in as their individual 64 bit sections
            elif multiEvent:
                outFile.write("{0:#0{1}x}   ".format(wrdCnt,6))
                lineArray = re.split(r'[ \n]', lineOne)
                tmpLinkAr = [x for x in lineArray[1:] if x !=""]
                countUp += toAdd
                if (wrdCnt % 3 == 0):
                    outFileTwo.write("start "+str(countr)+"\n")
                    countr+=1
                    link_out = ["0000"]*xLinks
                    countUp = 0
                    toAdd = 3
                else:
                    link_out = [""]*xLinks
                    toAdd = 4
                for lnk,link_in in enumerate(tmpLinkAr[:xLinks]):
                    cryStart = (lnk*NCrystalsPerLink)+countUp
                    print(lnkForCry,cryOnLnk,reg[lnkForCry][cryOnLnk].peak_reg)
                    for i in range(toAdd):
                        crySel = (toAdd-1-i)*4
                        if (cryStart+i >= 300):
                            link_out[lnk] = '0000'+link_out[lnk]
                            continue
                        j = int(link_in[2+(4*i)])
                        mycoeff = coeff[cryStart+i][j-1]
                        if outOneCrystal and (wrdCnt == 47 or wrdCnt == 44 or wrdCnt == 41) and i == 0:
                            checkProb = True
                            print("special one "+str(wrdCnt))
                            print("shift "+str(reg[lnkForCry][cryOnLnk].shift_reg[0])+" "+str(reg[lnkForCry][cryOnLnk].shift_reg[1])+" "+str(reg[lnkForCry][cryOnLnk].shift_reg[2])+" "+str(reg[lnkForCry][cryOnLnk].shift_reg[3]))
                            print("peak "+str(reg[lnkForCry][cryOnLnk].peak_reg[0])+" "+str(reg[lnkForCry][cryOnLnk].peak_reg[1]))
    
                        link_out[lnk] = TPG(int(link_in[2+crySel:6+crySel],16), mycoeff, reg[lnk][countUp+i],checkProb)+link_out[lnk]
                        checkProb = False
                        outFileTwo.write("Link "+str(lnk)+", Crystal "+str(countUp+i)+"\n")
                        outFileTwo.write("shift "+str(reg[lnk][countUp+i].shift_reg[0])+" "+str(reg[lnk][countUp+i].shift_reg[1])+" "+str(reg[lnk][countUp+i].shift_reg[2])+" "+str(reg[lnk][countUp+i].shift_reg[3])+"\n")
                        outFileTwo.write("peak "+str(reg[lnk][countUp+i].peak_reg[0])+" "+str(reg[lnk][countUp+i].peak_reg[1])+"\n")
                        outFileTwo.write("next"+"\n")
                        #print(countUp,i)
                    
    
                    outFile.write("0x"+"{0}".format(link_out[lnk])+"    ")
                for lnk in range(xLinks,48,1):
                    outFile.write("0x0000000000000000    ")
                outFile.write("\n")
                if outOneCrystal:
                    if (wrdCnt % 3 == wrdCntForCry):
                        print("adc "+str(wrdCnt // 3))
                        print("shift "+str(reg[lnkForCry][cryOnLnk].shift_reg[0])+" "+str(reg[lnkForCry][cryOnLnk].shift_reg[1])+" "+str(reg[lnkForCry][cryOnLnk].shift_reg[2])+" "+str(reg[lnkForCry][cryOnLnk].shift_reg[3]))
                        print("peak "+str(reg[lnkForCry][cryOnLnk].peak_reg[0])+" "+str(reg[lnkForCry][cryOnLnk].peak_reg[1]))
                        if wrdCntForCry == 1:
                            print("actOut "+str(link_out[lnkForCry][(cryOnLnk-3)*4:((cryOnLnk-3)*4)+4]))
                        elif wrdCntForCry == 2:
                            print("actOut "+str(link_out[lnkForCry][(cryOnLnk-7)*4:((cryOnLnk-7)*4)+4]))
                        else:
                            print("actOut "+str(link_out[lnkForCry][cryOnLnk*4:(cryOnLnk*4)+4]))
                
                elif (wrdCnt % 3 == 0):
                    print(wrdCnt)
                    print("shift "+str(reg[0][2].shift_reg[0])+" "+str(reg[0][2].shift_reg[1])+" "+str(reg[0][2].shift_reg[2])+" "+str(reg[0][2].shift_reg[3]))
                    print("peak "+str(reg[0][2].peak_reg[0])+" "+str(reg[0][2].peak_reg[1]))
    
                        
            #Here link_out/link_in are treated as the 192 bit whole
            else:
                if ( wrdCnt % 3 == 0 ):
                    link_out = ["00000000"]*xLinks
                    lineArray = re.split(r'[ \n]', lineOne)
                    tmpLinkAr = [x for x in lineArray[1:] if x !=""]
                    
                    for lnk,tpLink in enumerate(tmpLinkAr[:xLinks]):
                        link_in = "0x00000000000000000000000000000000"+tpLink[2:]
                        j = int(link_in[38])
                        mycoeff = coeff[lnk][j-1]
                        print("we about to do wrdCnt: "+str(wrdCnt))
                        link_out[lnk] = '000000000000000000000000000000000000'+TPG(int(link_in[38:42],16), mycoeff, reg[lnk],True)+link_out[lnk]
                        
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