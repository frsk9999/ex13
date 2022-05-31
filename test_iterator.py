#!/usr/bin/env python3


testlist=[1,2,3,4,[5,6,7,[8,9]]]

def gen(glist):
    for a in glist:
        if(type(a) is list): # nested list
            yield from gen(a)
        else:
            yield(a)


for i in gen(testlist):
    print(i)
