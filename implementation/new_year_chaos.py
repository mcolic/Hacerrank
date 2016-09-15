#!/bin/python

import sys


T = int(raw_input().strip())
for a0 in xrange(T):
    n = int(raw_input().strip())
    q = map(int,raw_input().strip().split(' '))
    # your code goes here
    start = 1
    bribe = 0
    step2 = 0

    for i in q:
        jumps = i - start

        if jumps > 2:
            bribe = "Too chaotic"
            break
        elif jumps > 0 and jumps != 2:
            bribe += 1
            step2 = 0
        elif jumps == 2:
            bribe += 2
            step2 += 1
        elif jumps <= 0 and step2 > 0:
            if jumps == 1 - step2:
                bribe += 1
            step2 = 0
        start += 1
    print bribe
