#!/bin/python


n, k, q = map(int, raw_input().strip().split())
arr = list(map(int, raw_input().strip().split()))

k %= n
arr = arr[-k:] + arr[:-k]

for i in range(q):
    print(arr[int(raw_input().strip())])
