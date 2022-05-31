#!/usr/bin/env python3 

class usrstr(str):
    def __del__(self):
        print(self,end=" ")

if __name__ == "__main__":
    hello :usrstr = usrstr("Hello")
    world :usrstr = usrstr("World")
    del hello,world
    print()
