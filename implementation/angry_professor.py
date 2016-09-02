#!/bin/python

import sys


t = int(raw_input().strip())
count = 0

for a0 in xrange(t):
    n,k = raw_input().strip().split(' ')
    n,k = [int(n),int(k)]
    a = map(int,raw_input().strip().split(' '))

    if len([i for i in a if i <=0]) < k:
        print 'YES'
    else:
        print 'NO'
