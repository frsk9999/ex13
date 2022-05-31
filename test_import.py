#!/usr/bin/env python3

import os
import compileall
import subprocess

comp = compile('print("test")','','exec') # こっちのコンパイルじゃない
eval(comp)

if(True == os.path.exists("./__pycache__/test_import.cpython-38.pyc")):
    exit(0)
    pass
else:
    print("compile to pyc")
    compileall.compile_file('test_import.py',ddir=os.environ['PWD'])

output = subprocess.run(["python3","__pycache__/test_import.cpython-38.pyc"],capture_output=True)
print("output:", output.stdout)
print("end")
