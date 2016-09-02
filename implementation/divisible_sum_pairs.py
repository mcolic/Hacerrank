#!/bin/python

import sys


n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
a = map(int,raw_input().strip().split(' '))

counter = 0
for i in range(n):
    for j in range(i):
        if (a[i]+a[j])%k==0:
            counter+=1
print counter
