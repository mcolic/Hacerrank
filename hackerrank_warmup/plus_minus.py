#!/bin/python

import sys


n = float(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

# print arr
neg = 0
pos = 0
zero = 0

for i in arr:
    if i < 0:
        neg += 1
    elif i > 0:
        pos += 1
    elif i == 0:
        zero += 1

print "{:.6f}".format(float(pos/n))
print "{:.6f}".format(float(neg/n))
print "{:.6f}".format(float(zero/n))
