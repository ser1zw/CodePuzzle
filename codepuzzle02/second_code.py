#!/usr/bin/env python
# -*- mode: python; coding: utf-8-unix -*- 

# http://cp1.nintendo.co.jp/2012
import re

class SimpleBars:
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
        self.update(data, ' ', ((0, ' '),))
        self.update(data, 'i', ((0, 'T'),))
        self.update(data, 'T', ((0, 'i'),))

        self.update(data, ' i', ((0, 'i'),))
        self.update(data, 'i ', ((1, 'i'),))

        self.update(data, 'iT', ((1, ' '),))
        self.update(data, 'Ti', ((0, ' '),))

        self.update(data, 'i i', ((1, ' '),))
        self.update(data, 'iTi', ((1, 'i'),))
        self.next_str_array = self.next_str_array[3:-3]

if __name__ == "__main__":
    bs = SimpleBars(' ' * 24)
    bs[8] = 'T'
    for i in range(30):
        print(bs.next())

