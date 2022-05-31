#!/usr/bin/env python3
# python3.8用
import gc
import sys
import sysconfig as syscon
import json
#from _testcapi import with_tp_del

#@with_tp_del
class test(str):
#    def __init__(self,val=None):# testの継承をstrからobjectに変えないと動かない
#        if val is None:
#            self.val = test(val=self) # for uncollectable
#        else:
#            self.val=val
#    def __tp_del__(self):
#        pass
    def __del__(self):
        print("del:",self)

gc.disable()                   # 一旦ガベコレオフ
gc.set_debug(gc.DEBUG_SAVEALL) # 一旦保存用

a=test("a")
b=test("b")
c=test("c")
a.next=[a,b]                   # 適当な場所に参照を作る
b.next=[a,b]
c.next=[a,b,c]
print(gc.is_tracked(c))        # gc対象ならtrue
print(gc.get_referents(c))     # 中身の表示
print(sys.getrefcount(c))      # 参照カウンタ値(本来は-1した値)
c.next=[]                      # cだけ参照を開放する
print(sys.getrefcount(c))      # 参照カウンタ値(本来は-1した値)
del a,b,c                      # ここでcだけ解放される(参照カウンタで解放)
print("deleted")
print("gc.gabage:",gc.garbage) # 空っぽ
print(gc.collect())            # gc実施してa,bが解放される

# 解放された結果がこちらに入る(jsonで出力)
print("gc.gabage:",json.dumps(gc.garbage,default=str,indent=2))

gc.enable() # ガベコレ再開
