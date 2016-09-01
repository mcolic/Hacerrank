#!/bin/python

import sys


hour, minute, second = raw_input().split(":")
h = int(hour)
s = second[:2]
time_ = second[2:]

if time_ == 'PM' and h < 12:
    print str(12 + h) + ":" + minute + ":"+s
elif time_ == 'AM' and h == 12:
    print '00'+":"+minute+":"+s
else:
    print h+":"+minute+":"+s
