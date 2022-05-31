#!/usr/bin/env python3

test=1

if(3 == test):
    print("test:",3)
elif(2 == test):
    print("test:",2)
else:
    print("test:",test)

test=2
match(test):
    case 2:
        print("test:",2)
    case 3:
        print("test:",3)
    case _:
        print("test:",test)
