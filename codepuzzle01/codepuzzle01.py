#!/usr/bin/env python
# -*- mode: python; coding: utf-8-unix -*- 

# http://cp1.nintendo.co.jp/
import sys

def lets_take_tea_break(m, e, n, c):
    if pow(m, e) % n == c:
        return str(m)
    return ""

if __name__ == "__main__":
    import sys
#    print("http://cp1.nintendo.co.jp/" +
#          lets_take_tea_break(*[int(i) for i in (sys.argv[1], 17, 3569, 915)]))

    for i in range(1, 10000):
        x = lets_take_tea_break(*[int(n) for n in (i, 17, 3569, 915)])
        if len(x) > 0:
            print("http://cp1.nintendo.co.jp/" + x)
            break

