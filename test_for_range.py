#!/usr/bin/env python3

# 最後になるか0.0になるまでループさせる
listall=["a",1,0.2,(3+5j),0.0,9]
for i in listall:
    if( 0.0 == i):
        break
    else:
        print("i:",i)
        continue

# 1から32までの3の倍数以外の値を足し算する
sum=0
for k in range(1,32):
    if( 0 == k % 3):
        pass
    else:
        sum += k
print("sum:",sum)

sum=0
for l in range(3,400,11):
    sum += l
print("sum:",sum)
