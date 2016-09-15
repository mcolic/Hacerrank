#!/bin/python

import sys


n = int(raw_input().strip())

factorial = 1;
for i in range(1, n + 1):
    factorial *= i
print factorial
