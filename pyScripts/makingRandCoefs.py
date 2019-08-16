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

xLinks = 28
NCrystalsPerLink = 11

#If all crystals are present so that no crystal coefficients need to be completely randomly generated
allPresent = True

"""
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
"""

coeff = np.array([[0xad6066, 0x0, 0x0],
[0xc26062, 0x0, 0x0],
[0xb1605c, 0x0, 0x0],
[0xd46074, 0x0, 0x0],
[0xa86064, 0x0, 0x0],
[0xa46062, 0x0, 0x0],
[0xb26070, 0x0, 0x0],
[0xaa6067, 0x0, 0x0],
[0xce6079, 0x0, 0x0],
[0xb56060, 0x0, 0x0],
[0xb2606b, 0x0, 0x0],
[0xad6064, 0x0, 0x0],
[0xad606e, 0x0, 0x0],
[0xb3605c, 0x0, 0x0],
[0xb9606f, 0x0, 0x0],
[0xb06071, 0x0, 0x0],
[0xae605d, 0x0, 0x0],
[0xb36069, 0x0, 0x0],
[0xa06057, 0x0, 0x0],
[0xa76061, 0x0, 0x0],
[0xb36069, 0x0, 0x0],
[0xad6066, 0x0, 0x0],
[0xae6061, 0x0, 0x0],
[0xad6068, 0x0, 0x0],
[0xa9605b, 0x0, 0x0],
[0xb86071, 0x0, 0x0],
[0xa16057, 0x0, 0x0],
[0xb2606a, 0x0, 0x0],
[0xc3606f, 0x0, 0x0],
[0xaa6056, 0x0, 0x0],
[0xad6068, 0x0, 0x0],
[0xa66063, 0x0, 0x0],
[0xaa605b, 0x0, 0x0],
[0xa46064, 0x0, 0x0],
[0xb1605d, 0x0, 0x0],
[0xba606d, 0x0, 0x0],
[0xa76067, 0x0, 0x0],
[0xac6059, 0x0, 0x0],
[0xa86061, 0x0, 0x0],
[0xb56065, 0x0, 0x0],
[0xb0606c, 0x0, 0x0],
[0xa1605e, 0x0, 0x0],
[0x9c6051, 0x0, 0x0],
[0xac6065, 0x0, 0x0],
[0xb06062, 0x0, 0x0],
[0xb0606e, 0x0, 0x0],
[0xb56065, 0x0, 0x0],
[0xa16063, 0x0, 0x0],
[0xaf6060, 0x0, 0x0],
[0xae6072, 0x0, 0x0],
[0xa4605f, 0x0, 0x0],
[0xb1605c, 0x0, 0x0],
[0xb0605c, 0x0, 0x0],
[0xb06066, 0x0, 0x0],
[0xa46065, 0x0, 0x0],
[0xaa605b, 0x0, 0x0],
[0xab606b, 0x0, 0x0],
[0xab6061, 0x0, 0x0],
[0xa16066, 0x0, 0x0],
[0xa16060, 0x0, 0x0],
[0xb36064, 0x0, 0x0],
[0x9e6065, 0x0, 0x0],
[0xaa606b, 0x0, 0x0],
[0xa8605b, 0x0, 0x0],
[0xb36072, 0x0, 0x0],
[0xa06065, 0x0, 0x0],
[0xa16059, 0x0, 0x0],
[0xa16068, 0x0, 0x0],
[0xa86067, 0x0, 0x0],
[0xa1605f, 0x0, 0x0],
[0xa96060, 0x0, 0x0],
[0xaa605d, 0x0, 0x0],
[0xaa605f, 0x0, 0x0],
[0xb06064, 0x0, 0x0],
[0xab6059, 0x0, 0x0],
[0xb0606a, 0x0, 0x0],
[0xb0606d, 0x0, 0x0],
[0xad6054, 0x0, 0x0],
[0xb16063, 0x0, 0x0],
[0xb16064, 0x0, 0x0],
[0xb66064, 0x0, 0x0],
[0xb1605c, 0x0, 0x0],
[0xb36062, 0x0, 0x0],
[0xaf6060, 0x0, 0x0],
[0xa76064, 0x0, 0x0],
[0xa76068, 0x0, 0x0],
[0xaa6064, 0x0, 0x0],
[0xa36061, 0x0, 0x0],
[0xad6069, 0x0, 0x0],
[0xaf6069, 0x0, 0x0],
[0xa46066, 0x0, 0x0],
[0xaf605d, 0x0, 0x0],
[0xa4605b, 0x0, 0x0],
[0xa46055, 0x0, 0x0],
[0xa86067, 0x0, 0x0],
[0xa86062, 0x0, 0x0],
[0xa66063, 0x0, 0x0],
[0xa7605c, 0x0, 0x0],
[0xa8606d, 0x0, 0x0],
[0xaf605f, 0x0, 0x0],
[0x9e604e, 0x0, 0x0],
[0xae6066, 0x0, 0x0],
[0xac6060, 0x0, 0x0],
[0xc16075, 0x0, 0x0],
[0xa96062, 0x0, 0x0],
[0xb06067, 0x0, 0x0],
[0xac6069, 0x0, 0x0],
[0xa76067, 0x0, 0x0],
[0xb56069, 0x0, 0x0],
[0x9e6056, 0x0, 0x0],
[0xb46067, 0x0, 0x0],
[0xa66056, 0x0, 0x0],
[0x99604f, 0x0, 0x0],
[0xb26059, 0x0, 0x0],
[0xae6064, 0x0, 0x0],
[0xa96056, 0x0, 0x0],
[0xb3606d, 0x0, 0x0],
[0x9c604e, 0x0, 0x0],
[0xa8605e, 0x0, 0x0],
[0xa66062, 0x0, 0x0],
[0xac6061, 0x0, 0x0],
[0xa5605a, 0x0, 0x0],
[0xa16060, 0x0, 0x0],
[0xae605c, 0x0, 0x0],
[0xa16062, 0x0, 0x0],
[0xad6067, 0x0, 0x0],
[0xa8605e, 0x0, 0x0],
[0xa56059, 0x0, 0x0],
[0xa56059, 0x0, 0x0],
[0xab6058, 0x0, 0x0],
[0xa9605a, 0x0, 0x0],
[0xa2605c, 0x0, 0x0],
[0xaf6066, 0x0, 0x0],
[0xa66054, 0x0, 0x0],
[0xa96061, 0x0, 0x0],
[0xa36066, 0x0, 0x0],
[0xac606f, 0x0, 0x0],
[0xa4605d, 0x0, 0x0],
[0xa4605e, 0x0, 0x0],
[0xa0605f, 0x0, 0x0],
[0xa36066, 0x0, 0x0],
[0x9d6060, 0x0, 0x0],
[0xa66065, 0x0, 0x0],
[0x92604a, 0x0, 0x0],
[0xad6068, 0x0, 0x0],
[0xa56065, 0x0, 0x0],
[0x9b605b, 0x0, 0x0],
[0xa8605c, 0x0, 0x0],
[0x93605d, 0x0, 0x0],
[0xa46064, 0x0, 0x0],
[0x9d604d, 0x0, 0x0],
[0xac605a, 0x0, 0x0],
[0x956044, 0x0, 0x0],
[0x9b605a, 0x0, 0x0],
[0xa7605e, 0x0, 0x0],
[0x9a604f, 0x0, 0x0],
[0xa26058, 0x0, 0x0],
[0xa56055, 0x0, 0x0],
[0x956049, 0x0, 0x0],
[0x9a6057, 0x0, 0x0],
[0xa46063, 0x0, 0x0],
[0x9b6059, 0x0, 0x0],
[0xa76066, 0x0, 0x0],
[0xa06065, 0x0, 0x0],
[0xa66061, 0x0, 0x0],
[0x98605f, 0x0, 0x0],
[0x9e6055, 0x0, 0x0],
[0xa0605a, 0x0, 0x0],
[0xa06058, 0x0, 0x0],
[0x9e6057, 0x0, 0x0],
[0xa56060, 0x0, 0x0],
[0x96604d, 0x0, 0x0],
[0x9b6063, 0x0, 0x0],
[0x8f6053, 0x0, 0x0],
[0x92604f, 0x0, 0x0],
[0xaa6058, 0x0, 0x0],
[0x976049, 0x0, 0x0],
[0xa6605c, 0x0, 0x0],
[0xa2605d, 0x0, 0x0],
[0x956056, 0x0, 0x0],
[0xa7605d, 0x0, 0x0],
[0xa5605e, 0x0, 0x0],
[0x9e605f, 0x0, 0x0],
[0x9f6063, 0x0, 0x0],
[0x956052, 0x0, 0x0],
[0xb3606b, 0x0, 0x0],
[0xa7605c, 0x0, 0x0],
[0x9a6055, 0x0, 0x0],
[0xa06053, 0x0, 0x0],
[0x9b605b, 0x0, 0x0],
[0x966056, 0x0, 0x0],
[0x9d6058, 0x0, 0x0],
[0x9f6055, 0x0, 0x0],
[0x9d6058, 0x0, 0x0],
[0xa0605b, 0x0, 0x0],
[0x9c6053, 0x0, 0x0],
[0x9d605e, 0x0, 0x0],
[0x91605d, 0x0, 0x0],
[0x9e6063, 0x0, 0x0],
[0xa26065, 0x0, 0x0],
[0xd06076, 0x0, 0x0],
[0xa56059, 0x0, 0x0],
[0xbf6065, 0x0, 0x0],
[0xc56070, 0x0, 0x0],
[0xcf6073, 0x0, 0x0],
[0xce6069, 0x0, 0x0],
[0x9c6058, 0x0, 0x0],
[0xc2606d, 0x0, 0x0],
[0xb2605e, 0x0, 0x0],
[0xb16066, 0x0, 0x0],
[0xad605a, 0x0, 0x0],
[0xa76068, 0x0, 0x0],
[0xab606c, 0x0, 0x0],
[0xb6606a, 0x0, 0x0],
[0xb5605e, 0x0, 0x0],
[0xb86077, 0x0, 0x0],
[0x9c6051, 0x0, 0x0],
[0xc56066, 0x0, 0x0],
[0x936055, 0x0, 0x0],
[0xa66059, 0x0, 0x0],
[0xbe6075, 0x0, 0x0],
[0x98604f, 0x0, 0x0],
[0xbd6070, 0x0, 0x0],
[0xa26056, 0x0, 0x0],
[0x92605d, 0x0, 0x0],
[0xa16056, 0x0, 0x0],
[0x916046, 0x0, 0x0],
[0x9e6061, 0x0, 0x0],
[0xad605f, 0x0, 0x0],
[0x9a6056, 0x0, 0x0],
[0xa16059, 0x0, 0x0],
[0x9a605d, 0x0, 0x0],
[0xa9605a, 0x0, 0x0],
[0x9c6059, 0x0, 0x0],
[0xb26066, 0x0, 0x0],
[0x9d604e, 0x0, 0x0],
[0x99604e, 0x0, 0x0],
[0xa16066, 0x0, 0x0],
[0x986050, 0x0, 0x0],
[0xa46053, 0x0, 0x0],
[0xa76056, 0x0, 0x0],
[0xa0605e, 0x0, 0x0],
[0xaa606b, 0x0, 0x0],
[0x96604d, 0x0, 0x0],
[0x936053, 0x0, 0x0],
[0xa2605c, 0x0, 0x0],
[0x986057, 0x0, 0x0],
[0x97605f, 0x0, 0x0],
[0x90604b, 0x0, 0x0],
[0x9b605a, 0x0, 0x0],
[0x936047, 0x0, 0x0],
[0x986052, 0x0, 0x0],
[0x936055, 0x0, 0x0],
[0x966051, 0x0, 0x0],
[0x966057, 0x0, 0x0],
[0xa0604e, 0x0, 0x0],
[0x936056, 0x0, 0x0],
[0xb96062, 0x0, 0x0],
[0x966053, 0x0, 0x0],
[0x96604a, 0x0, 0x0],
[0x936050, 0x0, 0x0],
[0x9d604f, 0x0, 0x0],
[0x946057, 0x0, 0x0],
[0x926046, 0x0, 0x0],
[0x996062, 0x0, 0x0],
[0x94605c, 0x0, 0x0],
[0x98605f, 0x0, 0x0],
[0x8c6047, 0x0, 0x0],
[0x8c6055, 0x0, 0x0],
[0x94605c, 0x0, 0x0],
[0x956062, 0x0, 0x0],
[0x98605e, 0x0, 0x0],
[0x986054, 0x0, 0x0],
[0xa76061, 0x0, 0x0],
[0x956050, 0x0, 0x0],
[0x956056, 0x0, 0x0],
[0x9a6057, 0x0, 0x0],
[0xaa605f, 0x0, 0x0],
[0xb26065, 0x0, 0x0],
[0x9a604d, 0x0, 0x0],
[0x98605e, 0x0, 0x0],
[0x8e6050, 0x0, 0x0],
[0x9a605a, 0x0, 0x0],
[0x98605e, 0x0, 0x0],
[0x966055, 0x0, 0x0],
[0x95604b, 0x0, 0x0],
[0x956048, 0x0, 0x0],
[0x94605a, 0x0, 0x0],
[0x976055, 0x0, 0x0],
[0x916052, 0x0, 0x0],
[0x92604f, 0x0, 0x0],
[0xa96068, 0x0, 0x0],
[0x8f6049, 0x0, 0x0],
[0xa06069, 0x0, 0x0],
[0x93604e, 0x0, 0x0],
[0x986062, 0x0, 0x0],
[0xb2606d, 0x0, 0x0],
[0x94604a, 0x0, 0x0],
[0x956060, 0x0, 0x0],
[0x94604d, 0x0, 0x0]])

prob1stAr = [[[131, 0.020833333333333332],
  [133, 0.041666666666666664],
  [134, 0.020833333333333332],
  [139, 0.020833333333333332],
  [140, 0.020833333333333332],
  [146, 0.020833333333333332],
  [154, 0.020833333333333332],
  [157, 0.041666666666666664],
  [158, 0.020833333333333332],
  [161, 0.020833333333333332],
  [172, 0.020833333333333332],
  [173, 0.0625],
  [174, 0.020833333333333332],
  [177, 0.020833333333333332],
  [180, 0.020833333333333332],
  [181, 0.020833333333333332],
  [183, 0.041666666666666664],
  [186, 0.041666666666666664],
  [190, 0.020833333333333332],
  [191, 0.020833333333333332],
  [192, 0.020833333333333332],
  [193, 0.020833333333333332],
  [194, 0.020833333333333332],
  [195, 0.020833333333333332],
  [197, 0.020833333333333332],
  [203, 0.020833333333333332],
  [207, 0.020833333333333332],
  [208, 0.041666666666666664],
  [210, 0.020833333333333332],
  [215, 0.020833333333333332],
  [222, 0.020833333333333332],
  [223, 0.041666666666666664],
  [224, 0.020833333333333332],
  [229, 0.020833333333333332],
  [232, 0.041666666666666664],
  [233, 0.020833333333333332],
  [242, 0.020833333333333332],
  [245, 0.020833333333333332],
  [254, 0.020833333333333332]],
 [[5, 0.6666666666666666], [6, 0.3333333333333333]],
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

prob2ndAr = [[[186, 186, 0.3333333333333333],
  [232, 232, 0.3333333333333333],
  [245, 245, 0.3333333333333333]],
 [[5, 4, 0.6666666666666666], [6, 5, 0.3333333333333333]],
 [[97, 148, 0.3333333333333333],
  [113, 156, 0.3333333333333333],
  [117, 158, 0.3333333333333333]]]

prob3rdAr = [[[131, None, 196, 1.0],
  [133, None, 200, 1.0],
  [134, None, 201, 1.0],
  [139, None, 208, 1.0],
  [140, None, 210, 1.0],
  [146, None, 219, 1.0],
  [154, None, 231, 1.0],
  [157, None, 235, 1.0],
  [158, None, 237, 1.0],
  [161, None, 242, 1.0],
  [172, None, 129, 1.0],
  [173, None, 129, 0.3333333333333333],
  [173, None, 130, 0.6666666666666666],
  [174, None, 131, 1.0],
  [177, None, 132, 1.0],
  [180, None, 135, 1.0],
  [181, None, 136, 1.0],
  [183, None, 137, 1.0],
  [186, None, 140, 1.0],
  [186, 186, 139, 1.0],
  [190, None, 143, 1.0],
  [191, None, 143, 1.0],
  [192, None, 144, 1.0],
  [193, None, 144, 1.0],
  [194, None, 146, 1.0],
  [195, None, 147, 1.0],
  [197, None, 148, 1.0],
  [203, None, 152, 1.0],
  [207, None, 156, 1.0],
  [208, None, 156, 1.0],
  [210, None, 157, 1.0],
  [215, None, 161, 1.0],
  [222, None, 166, 1.0],
  [223, None, 167, 1.0],
  [224, None, 168, 1.0],
  [229, None, 171, 1.0],
  [232, None, 174, 1.0],
  [232, 232, 174, 1.0],
  [233, None, 175, 1.0],
  [242, None, 182, 1.0],
  [245, 245, 184, 1.0],
  [254, None, 191, 1.0]],
 [[5, None, 1, 0.6333333333333333],
  [5, None, 2, 0.36666666666666664],
  [5, 4, 1, 1.0],
  [6, None, 2, 0.9333333333333333],
  [6, None, 3, 0.06666666666666667],
  [6, 5, 2, 1.0]],
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

prob4thAr = [[[131, 196, 1.0],
  [133, 200, 1.0],
  [134, 201, 1.0],
  [139, 208, 1.0],
  [140, 210, 1.0],
  [146, 219, 1.0],
  [154, 231, 1.0],
  [157, 235, 1.0],
  [158, 237, 1.0],
  [161, 242, 1.0],
  [172, 129, 1.0],
  [173, 129, 0.3333333333333333],
  [173, 130, 0.6666666666666666],
  [174, 131, 1.0],
  [177, 132, 1.0],
  [180, 135, 1.0],
  [181, 136, 1.0],
  [183, 137, 1.0],
  [186, 140, 0.5],
  [186, 139, 0.5],
  [190, 143, 1.0],
  [191, 143, 1.0],
  [192, 144, 1.0],
  [193, 144, 1.0],
  [194, 146, 1.0],
  [195, 147, 1.0],
  [197, 148, 1.0],
  [203, 152, 1.0],
  [207, 156, 1.0],
  [208, 156, 1.0],
  [210, 157, 1.0],
  [215, 161, 1.0],
  [222, 166, 1.0],
  [223, 167, 1.0],
  [224, 168, 1.0],
  [229, 171, 1.0],
  [232, 174, 1.0],
  [233, 175, 1.0],
  [242, 182, 1.0],
  [245, 184, 1.0],
  [254, 191, 1.0]],
 [[5, 1, 0.65625], [5, 2, 0.34375], [6, 2, 0.9375], [6, 3, 0.0625]],
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


minNames = ["minlE","minnF","minfT"]
maxNames = ["maxlE","maxnF","maxfT"]
minmaxDict = {}

for i in range(3):
    minmaxDict[minNames[i]] = min(min(prob3rdArNP[i][np.where((prob3rdArNP[i])[:,2] != None),2][0]),min(min(prob3rdArNP[i][np.where((prob3rdArNP[i])[:,1] != None),1][0]),min(prob3rdArNP[i][np.where((prob3rdArNP[i])[:,0] != None),0][0])))
    minmaxDict[maxNames[i]] = max(max(prob3rdArNP[i][np.where((prob3rdArNP[i])[:,2] != None),2][0]),max(max(prob3rdArNP[i][np.where((prob3rdArNP[i])[:,1] != None),1][0]),max(prob3rdArNP[i][np.where((prob3rdArNP[i])[:,0] != None),0][0])))

    
 
def con1stCo():
    lE = int(np.random.choice(prob1stArNP[0][:,0],p=prob1stArNP[0][:,1]))
    nF = int(np.random.choice(prob1stArNP[1][:,0],p=prob1stArNP[1][:,1]))
    fT = int(np.random.choice(prob1stArNP[2][:,0],p=prob1stArNP[2][:,1]))
    return [lE,nF,fT]

def con2ndCo(coOne):
    
    lE = coOne[0]
    nF= coOne[1]-1
    if nF< minmaxDict[minNames[1]]:
        nF= minmaxDict[minNames[1]]
    elif nF> minmaxDict[maxNames[1]]:
        nF= minmaxDict[minNames[1]]
    fT = coOne[2]+51-((coOne[2]-97)//2)
    if fT < minmaxDict[minNames[2]]:
        fT = minmaxDict[minNames[2]]
    elif fT > minmaxDict[maxNames[2]]:
        fT = minmaxDict[minNames[2]]
    return [lE,nF,fT]
    
def con3rdCo(coOne):
    lE=0
    nF=0
    fT=0
    if coOne[0] < min(prob1stArNP[0][:,0]):
        tmpAr = np.array([ar[1:] for ar in prob4thArNP[0] if ar[0]==(min(prob1stArNP[0][:,0]))])
        lE = int(np.random.choice(tmpAr[:,0],p=tmpAr[:,1]))
    elif coOne[0] > max(prob1stArNP[0][:,0]):
        tmpAr = np.array([ar[1:] for ar in prob4thArNP[0] if ar[0]==(max(prob1stArNP[0][:,0]))])
        lE = int(np.random.choice(tmpAr[:,0],p=tmpAr[:,1]))
    else:
        for i in range(1+int(min(coOne[0] - min(prob1stArNP[0][:,0]),max(prob1stArNP[0][:,0])- coOne[0]))):
            tmpArUp = np.array([ar[1:] for ar in prob4thArNP[0] if ar[0]==(coOne[0]+i)])
            tmpArDown = np.array([ar[1:] for ar in prob4thArNP[0] if ar[0]==(coOne[0]-i)])
            if tmpArUp.size:    
                lE = int(np.random.choice(tmpArUp[:,0],p=tmpArUp[:,1]))
                break
            elif tmpArDown.size:
                lE = int(np.random.choice(tmpArDown[:,0],p=tmpArDown[:,1]))
                break

    if coOne[1] < min(prob1stArNP[1][:,0]):
        tmpAr = np.array([ar[1:] for ar in prob4thArNP[1] if ar[0]==(min(prob1stArNP[1][:,0]))])
        nF = int(np.random.choice(tmpAr[:,0],p=tmpAr[:,1]))
    elif coOne[1] > max(prob1stArNP[1][:,0]):
        tmpAr = np.array([ar[1:] for ar in prob4thArNP[1] if ar[0]==(max(prob1stArNP[1][:,0]))])
        nF = int(np.random.choice(tmpAr[:,0],p=tmpAr[:,1]))
    else:
        for i in range(1+int(min(coOne[1] - min(prob1stArNP[1][:,0]),max(prob1stArNP[1][:,0])- coOne[1]))):
            tmpArUp = np.array([ar[1:] for ar in prob4thArNP[1] if ar[0]==(coOne[1]+i)])
            tmpArDown = np.array([ar[1:] for ar in prob4thArNP[1] if ar[0]==(coOne[1]-i)])
            if tmpArUp.size:    
                nF = int(np.random.choice(tmpArUp[:,0],p=tmpArUp[:,1]))
                break
            elif tmpArDown.size:
                nF = int(np.random.choice(tmpArDown[:,0],p=tmpArDown[:,1]))
                break

    if coOne[2] < min(prob1stArNP[2][:,0]):
        tmpAr = np.array([ar[1:] for ar in prob4thArNP[2] if ar[0]==(min(prob1stArNP[2][:,0]))])
        fT = int(np.random.choice(tmpAr[:,0],p=tmpAr[:,1]))
    elif coOne[2] > max(prob1stArNP[2][:,0]):
        tmpAr = np.array([ar[1:] for ar in prob4thArNP[2] if ar[0]==(max(prob1stArNP[2][:,0]))])
        fT = int(np.random.choice(tmpAr[:,0],p=tmpAr[:,1]))
    else:
        for i in range(1+int(min(coOne[2] - min(prob1stArNP[2][:,0]),max(prob1stArNP[2][:,0])- coOne[2]))):
            tmpArUp = np.array([ar[1:] for ar in prob4thArNP[2] if ar[0]==(coOne[2]+i)])
            tmpArDown = np.array([ar[1:] for ar in prob4thArNP[2] if ar[0]==(coOne[2]-i)])
            if tmpArUp.size:    
                fT = int(np.random.choice(tmpArUp[:,0],p=tmpArUp[:,1]))
                break
            elif tmpArDown.size:
                fT = int(np.random.choice(tmpArDown[:,0],p=tmpArDown[:,1]))
                break
    return [lE,nF,fT]
if allPresent:
    coeffAr= np.zeros([300, 3],dtype=int)
else:
    coeffAr= np.zeros([xLinks*NCrystalsPerLink, 3],dtype=int)
    impLinks = [(NCrystalsPerLink*i)+1 for i in range(xLinks)]
    iLCount = 0
    doneLinks = [4,7,9]
if allPresent:
    for i,co in enumerate(coeff[:,0]):
        hco = hex(co)[2:].zfill(6)
        tmpB = con2ndCo([int(hco[:2],16),int(hco[2],16),int(hco[3:],16)])
        tmpC = con3rdCo([int(hco[:2],16),int(hco[2],16),int(hco[3:],16)])
        #print(tmpB,tmpC)
        coeffAr[i] = [co,int('{0:08b}'.format(tmpB[0])+'{0:04b}'.format(tmpB[1])+'{0:012b}'.format(tmpB[2]),2),int('{0:08b}'.format(tmpC[0])+'{0:04b}'.format(tmpC[1])+'{0:012b}'.format(tmpC[2]),2)]
else:
    for i in range(xLinks*NCrystalsPerLink):
        if i in impLinks:
            
            if iLCount in doneLinks:
                coeffAr[i] = coeff[iLCount]
            else:
                tmpA = [int('{0:024b}'.format(coeff[iLCount][0])[:8],2),int('{0:024b}'.format(coeff[iLCount][0])[8:12],2),int('{0:024b}'.format(coeff[iLCount][0])[12:24],2)]
                tmpB = con2ndCo(tmpA)
                coeffAr[i] = [coeff[iLCount][0],int('{0:08b}'.format(tmpB[0])+'{0:04b}'.format(tmpB[1])+'{0:012b}'.format(tmpB[2]),2),coeff[iLCount][2]]
            iLCount += 1
        else:
            tmpA = con1stCo()
            tmpB = con2ndCo(tmpA)
            tmpC = con3rdCo(tmpA)
            coeffAr[i] = [int('{0:08b}'.format(tmpA[0])+'{0:04b}'.format(tmpA[1])+'{0:012b}'.format(tmpA[2]),2),int('{0:08b}'.format(tmpB[0])+'{0:04b}'.format(tmpB[1])+'{0:012b}'.format(tmpB[2]),2),int('{0:08b}'.format(tmpC[0])+'{0:04b}'.format(tmpC[1])+'{0:012b}'.format(tmpC[2]),2)]

if oneD:
    outFile = open("{0}links{1}crystals_Gen_coeffArrays_OneD_Fixd.txt".format(xLinks,NCrystalsPerLink),"w")
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
    if allPresent:
        outFile = open("{0}links{1}crystals_Gen_coeffArrays_Fixd_aP.txt".format(xLinks,NCrystalsPerLink),"w")
        outFile.write("C coeff:\n")
        outFile.write("static const uint24_t coeff[300][3] = {{"+"0x"+hex(coeffAr[0][0])[2:].zfill(6)+", "+"0x"+hex(coeffAr[0][1])[2:].zfill(6)+", "+"0x"+hex(coeffAr[0][2])[2:].zfill(6)+"}")

    else:
        outFile = open("{0}links{1}crystals_Gen_coeffArrays_Fixd.txt".format(xLinks,NCrystalsPerLink),"w")
        outFile.write("C coeff:\n")
        outFile.write("static const uint24_t coeff[{0}][3] = {{".format(xLinks*NCrystalsPerLink)+hex(coeffAr[0][0])+", "+hex(coeffAr[0][1])+", "+hex(coeffAr[0][2])+"}")
    for ar in coeffAr[1:]:
        outFile.write(",\n{"+"0x"+hex(ar[0])[2:].zfill(6))
        for element in ar[1:]:
            outFile.write(", "+"0x"+hex(element)[2:].zfill(6))
        outFile.write("}")
    outFile.write("};\n")
            
    outFile.write("Python coeff:\n")
    outFile.write("coeff = [["+"0x"+hex(coeffAr[0][0])[2:].zfill(6)+", "+"0x"+hex(coeffAr[0][1])[2:].zfill(6)+", "+"0x"+hex(coeffAr[0][2])[2:].zfill(6)+"]")
    for ar in coeffAr[1:]:
        outFile.write(",\n["+"0x"+hex(ar[0])[2:].zfill(6))
        for element in ar[1:]:
            outFile.write(", "+"0x"+hex(element)[2:].zfill(6))
        outFile.write("]")
    outFile.write("]\n")

outFile.close()
