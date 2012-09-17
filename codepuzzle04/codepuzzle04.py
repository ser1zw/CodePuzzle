#!/usr/bin/env python
# -*- mode: python; coding: utf-8-unix -*- 

# http://cp1.nintendo.co.jp/inverse
from second_code import Bars
from third_code import decode_morse

src = "ITT TI I T TIii"
bs = Bars(src)
prev = None
for i in range(1000):
    prev = str(bs)
    bs.next()
    if str(bs) == src:
        break
    else:
        prev = None

if prev == None:
    print("Not found")
else:
    print(decode_morse(str(prev)))


