#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
big_sum = 0

for i in arr:
    big_sum += i


print big_sum
