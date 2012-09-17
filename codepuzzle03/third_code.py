#!/usr/bin/env python
# -*- mode: python; coding: utf-8-unix -*- 
import re

def decode_morse(s):
    morse = {
        "iIII" : "j", "iIii" : "l", "iIIi" : "p", "IIiI" : "q",
        "iiiI" : "v", "IiiI" : "x", "IiII" : "y", "IIii" : "z",
        "Iiii" : "b", "IiIi" : "c", "iiIi" : "f", "iiii" : "H",
        "Iii" : "d", "IIi" : "g", "IiI" : "k", "III" : "o",
        "iIi" : "r", "iii" : "s", "iiI" : "u", "iII" : "w",
        "iI" : "a", "Ii" : "n", "II" : "m", "ii" : "i",
        "i" : "e", "I" : "t"
        }

    regex = re.compile("\s+")
    code = regex.split(s.strip())
    decoded = []
    for c in code:
        decoded.append(morse[c])

    return "".join(decoded)


