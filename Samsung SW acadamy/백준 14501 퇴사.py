# -*- conding: utf-8 -*-

'''
Author : gksrbans123@gmail.com
Date : 2021-04-05
URL : https://www.acmicpc.net/problem/14501
Type : 나도 퇴사좀
'''

import sys

sys.stdin = open('input.txt', 'r')

n = int(input())

t = [0]
p = [0]
# n + 1일 까지 계산합니다.
d = [0] * (n+3)
result = 0

for i in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)

#print(t)
#print(p)

for i in range(1, n+1):
    if i + t[i] <= n + 1:
        d[i+t[i]] = max(d[i+t[i]], d[i] + p[i])
        result = max(result, d[i+t[i]])

    d[i + 1] = max(d[i + 1], d[i])
    result = max(result, d[i+1])

print(result)