import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
sum_ = 0

for i in arr:
    sum_ += i

print sum_
