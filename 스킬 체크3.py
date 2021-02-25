# -*- conding: utf-8 -*-

'''
Author : gksrbans123@gmail.com
Date : 2021-02-26
URL : https://programmers.co.kr/skill_checks/252929
Type : 스킬을 체크해보자
'''

from itertools import permutations

A, B = [5, 1, 3, 7], [2, 2, 6, 8]
answer = 0
A.sort(reverse=True)
B.sort()
i = 0

while B:
    if A[-1] < B[0]:
        answer += 1
        A.pop(-1)
    B.pop(0)

print(answer)