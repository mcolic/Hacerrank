#!/bin/python

import sys


n = int(raw_input().strip())
a = []
for a_i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    a.insert(a_i, a_temp)




# print a
d1 = 0
d2 = 0

for i in range(0,n):
    d1 += a[i][i]
    d2 += a[n-1-i][i]

print abs(d1-d2)
