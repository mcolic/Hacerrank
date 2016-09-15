#!/bin/python


for i in range(input()):
    stone_num = []
    n = input()
    a = input()
    b = input()
    a, b = min(a, b), max(a, b)
    min_ = (n - 1) * a
    for i in range(0, n):
        step = min_ - a * i + b * i
        if step not in stone_num:
            stone_num.append(step)
    print ' '.join(map(str, stone_num))
