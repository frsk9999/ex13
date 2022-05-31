#!/usr/bin/env python3 
import gc

class usrstr(str):
    def __del__(self):
        pass
    def __str__(self):
        return "hello world!!"
if __name__ == "__main__":
    gc.disable()
    gc.set_debug(gc.DEBUG_SAVEALL)
    test=usrstr("")
    test=[str(test)]
    test.append(test)
    del test
    gc.collect()
    print(gc.garbage)
