# -*- conding: utf-8 -*-

'''
Author : gksrbans123@gmail.com
Date : 2021-02-13
URL : https://programmers.co.kr/learn/courses/30/lessons/72411
Type : 2021 카카오 kakakao
'''

from itertools import combinations
from collections import defaultdict

orders, course = ["XYZ", "XWY", "WXA"], [2, 3, 4]

arr = defaultdict(lambda: 0)
answer = []

for x in course:
    arr.clear()
    for i in orders:
        #print(sorted(i))
        combi = combinations(list(i), x)
        for j in combi:
            arr[''.join(sorted(j))] += 1
    sorted(arr.items(), key=lambda v:v[1], reverse=True)
    print(arr)
    try:
        num = max(arr.values())
    except:
        num = 0
    if num >= 2:
        for k, v in arr.items():
            if v == num:
                answer.append(k)

print(sorted(answer))

