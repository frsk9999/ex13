#!/usr/bin/env python3

test=0
while(4>test):
    print("test:",test)
    test+=1
    if(4 == test):
        print("test:",test)
        break
else:
    print("else:",test)
