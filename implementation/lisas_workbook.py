#!/bin/python

chapter, prob_per_page = map(int, raw_input().strip().split(' '))
problems =  map(int, raw_input().strip().split(' '))


special_problems = 0
page = 1

for i in range(1,len(problems)+1):
    for j in range(1,problems[i-1]+1):
        if j == page:
            special_problems += 1
        if j < problems[i-1]:
            if j % prob_per_page == 0:
                page += 1
    page += 1



print special_problems
