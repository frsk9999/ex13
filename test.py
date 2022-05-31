#!/usr/bin/env python3 

def printx(text):
    print(text,end='')

class Hello:
    hellotext="" # publicへんすう
    worldtext="" # publicへんすう
    def __init__(self):
        self.hellotext='he'
    def __del__(self):
        self.worldtext = self.worldtext + 'ld'

class World(Hello): # 継承もできる
    def __init__(self):
        super().__init__() # 親クラスのinitを呼ぶ
        self.hellotext = self.hellotext + 'llo'
        for i in self.hellotext:
            if i == 'h':
                printx(i.upper())
            else:
                printx(i)
    def __del__(self):
        self.worldtext='wor'
        super().__del__() # 親クラスのdelを呼ぶ
        self.worldtext = self.worldtext + "!!\n"
        for i in self.worldtext:
            if i == 'l':
                printx('ke')
            else:
                printx(i)
    def __str__(self): # printに渡されるとここが使われる
        return ' '

if __name__ == "__main__":
    test = World()
    printx(test)
    del test
