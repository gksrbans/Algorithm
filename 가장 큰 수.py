# -*- conding: utf-8 -*-

'''
Author : gksrbans123@gmail.com
Date : 2020-10-19
URL : https://programmers.co.kr/learn/courses/30/lessons/42746
Type : Sort
'''

import functools

def cmp(a, b):
    num1 = int(a + b)
    num2 = int(b + a)

    if num1 > num2:
        return 1
    elif num1 < num2:
        return -1
    else:
        return 0


def solution(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(cmp), reverse=True)
    n = str(''.join(n))

    if int(n) == 0:
        n = '0'
    return n

# 파이썬 2에서 sorted는 cmp인자를 받아서 정렬할 수 있었었으나, 파이썬 3에서는 key값에 functools를 이용해 정렬가능.

#################################################################

# 1차 코딩 (permutations 코드, 시간초과로 시간복잡도 매우 구림)
# import itertools
#
# def solution(numbers):
#     length = len(numbers)
#     p = itertools.permutations(numbers, length)
#     answer = []
#     temp = ""
#
#     for i in p:
#         for j in range(length):
#             temp += str(i[j])
#         answer.append(temp)
#         temp = ""
#     return max(answer)