#!/usr/bin/env python
# -*- mode: python; coding: utf-8-unix -*- 

# http://cp1.nintendo.co.jp/moon
import re

class Bars:
    def __init__(self, init_str):
        self.data = list(init_str)
        return

    def __len__(self):
        return len(self.data)

    def __setitem__(self, index, item):
        self.data[index] = item
        return

    def __str__(self):
        return ''.join(self.data)

    def next(self):
        self.create_next()
        self.data = self.next_str_array
        return str(self)

    def update(self, data, pattern, conv_list):
        regex = re.compile(pattern)
        s = "".join(data)
        pos = 0
        while True:
            m = regex.search(s, pos)
            if m == None:
                break
            else:
                for delta, replacement in conv_list:
                    i = m.start() + delta
                    self.next_str_array[i] = replacement
                pos = m.start() + 1

    def create_next(self):
        a = list(self.data[-3]) + list(self.data[-2]) + list(self.data[-1])
        b = list(self.data[0]) + list(self.data[1]) + list(self.data[2])
        data = a + self.data + b
        self.next_str_array = list(' ' * len(data))

        for i in range(1, len(self.next_str_array) - 2):
            c = self.update_box(data[i], data[i + 1], data[i + 2])
            self.next_str_array[i + 1] = c

        self.next_str_array = self.next_str_array[3:-3]
        return

    def is_black(self, c):
        return (c == 'i' or c == 'I')
    
    def update_box(self, left, center, right):
        # you may use this table :-)
        table = [{ " ":" ", "i":"T", "T":"i", "I":"I" },
                 { " ":"i", "i":"I", "T":" ", "I":"T" }]
        count = 0
        if self.is_black(left): count += 1
        if self.is_black(right): count += 1

        return table[count % 2][center]


if __name__ == "__main__":
    bs = Bars("I    IT ii  i I   I i   i   I  T")
    bs.next()
    print(str(bs))
    bs.next()
    print(str(bs))
