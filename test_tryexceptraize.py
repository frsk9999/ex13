#!/usr/bin/env python3

class TestError(Exception):
    pass

def func():
    raise TestError("なんかよくわからないがError")

try:
    func()
except TestError as a:
    print(a)
finally:
    print("end")

