# -*- conding: utf-8 -*-

'''
Author : gksrbans123@gmail.com
Date : 2021-03-28
URL : URL : https://programmers.co.kr/learn/courses/30/lessons/72411
Type : Permutations
'''

import math
import collections
import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    answer = 0
    x = list(input())
    temp = list(x)
    standard = temp[0]

    while len(x) > 0:
        arr = []
        temp = list(x)
        standard = temp[0]
        L = len(temp)

        for i in temp:
            if i < standard:
                arr.append(i)

        y = collections.Counter(arr)

        #print(y , '작은거')
        for i in y.keys():
            #print(i)
            new = collections.Counter(temp) - collections.Counter(i)
            #print(new, '뺀거')
            basic = math.factorial(L-1)
            for j in new.values():
                basic = basic // math.factorial(j)
            #print(basic, '정답')
            answer += basic
        x = x[1:]
    print('#{} {}'.format(test_case, answer))
