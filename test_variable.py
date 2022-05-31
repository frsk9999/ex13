#!/usr/bin/env python3

# 型を宣言して定義するイメージ
test1: int=3
print("test1(int):",test1)
test2: str="test"
print("test2(str):",test2)
test3: bool=False
print("test3(bool):",test3)
test4: bytes=b'\x42\x79\x74\x65\x73'
print("test4(bytes):",test4)
test5: complex=(3+5j)-(-2+9j)
print("test5(complex):",test5)
test6: float=0.4
print("test6(float):",test6)
test7: list=[1,"test",["a",0x36,(3+4j)],0.5]
print("test7(list):",test7)
test8: dict={"key": [9,"aaa",(2-5j)] }
print("test8(dict):",test8)
print("key:",test8['key'])

test9: int={"safe": "out"} # 所詮は飾りで代入処理で上書きされてしまう
print(type(test9))
print("test9(int?):",test8)

""" エラーを検出したい？そうだね、mypyだね """
