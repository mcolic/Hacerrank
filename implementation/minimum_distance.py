#!/bin/python

import sys


n = int(raw_input().strip())
A = map(int,raw_input().strip().split(' '))

difference=n+1
for i in range(n):
    for j in range(i,n):
        if int(A[j])==int(A[i]) and (abs(j-i)<difference) and j!=i:
            difference=abs(j-i)
if difference==n+1:
    difference=-1
print difference
