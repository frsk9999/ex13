#!/usr/bin/env python3

# いろんな型を同じ変数に代入できる
test=3
test="test"
test=False
test=b'\x42\x79\x74\x65\x73'
test=(3+5j)-(-2+9j)
test=0.4
test=[1,"test",["a",0x36,(3+4j)],0.5]
test={"key": [9,"aaa",(2-5j)] }

print("test:", test) # 最後に入れたものが表示される
