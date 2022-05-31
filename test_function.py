#!/usr/bin/env python3

def function(x=4):
    if(0==x):
        return 0
    else:
        print("test:",function(x-1))
        return x

function()
