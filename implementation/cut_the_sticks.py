#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))


while (len(arr)>0):
    print len(arr)
    arr = sorted(arr)
    s = arr[0]
    for i in range(0,len(arr)):
        arr[i] = arr[i] - s
    arr = [int(x) for x in arr if (x>0)]
