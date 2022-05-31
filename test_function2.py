#!/usr/bin/env python3

def func2(x,/,y,z,*,a):
    print("x:",x,"y:",y,"z:",z,"a:",a)

func2(1,3,z="z",a="y")
