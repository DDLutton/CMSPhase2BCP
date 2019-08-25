#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 16:57:43 2019

@author: dylanlutton
"""

#This file is so I can put a location in from the diff checker and it can direct me to the right places in all the types of files I want it to
#Assuming a fake event to initialize things where ev = -1, j=-10 to -1

#Changes it for initAllEvents
initAllEvents = True

#ev,j,wrdCnt % 3, lnk,cry
loc = (0, 3, 2, 0, [7])

#Two types of files:the data input file from Nancy
#and the inp/out files in hex that are made by me from the data file

#Data file
if initAllEvents:
    if loc[0] % 2 == 0:
        print("For the data input file go to what is listed as event {}".format((loc[0]+1)))
        for cry in loc[4]:
            print("Next go to what is listed as crystal {}".format((cry+1)+(loc[3]*11)))
            print("Then, starting at zero, go to adc input {}".format(loc[1] % 10))
        print("")
        print("")
    else:
        print("This is the fake event preceding what is listed as event {}".format((loc[0]+3) // 2))
        for cry in loc[4]:
            print("Counting from 1 it's on crystal {}".format((cry+1)+(loc[3]*11)))
            print("Then, starting at zero, it's adc input {}".format(loc[1] % 10))
        print("")
        print("")


else:
    print("For the data input file go to what is listed as event {}".format(loc[0]+1))
    for cry in loc[4]:
        print("Next go to what is listed as crystal {}".format((cry+1)+(loc[3]*11)))
        print("Then, starting at zero, go to adc input {}".format(loc[1] % 10))
    print("")
    print("")

#inp/out files
print("For the inp/out files it will be the {0} crystal on link {1} on hex number {2}".format(loc[4][0],loc[3],hex((30+(loc[1]*3))+loc[2])))
for cry in loc[4][1:]:
    print("also crystal {}".format(cry))


