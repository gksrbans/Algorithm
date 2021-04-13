# -*- conding: utf-8 -*-

'''
Author : gksrbans123@gmail.com
Date : 2021-04-05
URL : https://www.acmicpc.net/problem/14888
Type : ?
'''

import sys

sys.stdin = open('input.txt', 'r')

N = int(input())
nums = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

min_, max_ = 1e9, -1e9

def DFS(i, res, add, sub, mul, div):
    global max_, min_
    if i == N:
        max_ = max(res, max_)
        min_ = min(res, min_)
        return

    else:
        if add:
            DFS(i+1, res+nums[i], add-1, sub, mul, div)
        if sub:
            DFS(i + 1, res - nums[i], add, sub-1, mul, div)
        if mul:
            DFS(i+1, res*nums[i], add, sub, mul-1, div)
        if div:
            DFS(i+1, int(res/nums[i]), add, sub, mul, div-1)

DFS(1, nums[0], add, sub, mul, div)
print(max_)
print(min_)



