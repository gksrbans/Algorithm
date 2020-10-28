# -*- conding: utf-8 -*-

'''
Author : gksrbans123@gmail.com
Date : 2020-10-25
URL : https://programmers.co.kr/learn/courses/30/lessons/42862
Type : Greedy
'''

from collections import deque


def solution(number, k):
    q = deque([])

    for i in number:
        while q and q[-1] < i and k > 0:
            q.pop()
            k -= 1
        q.append(i)

    while k > 0:
        q.pop()
        k -= 1
    return ''.join(q)

#########################################################

# while 문을 돌리면서 가장큰 숫자가 맨 앞으로 오게 만들어준다. 자리를 옮겼으면, 카운팅
# Refer: https://gurumee92.tistory.com/162

# 첫 번째 코드 (시간초과)
# def solution(number, k):
#     count = 0
#     n = list(number)
#
#     while (count < k):
#         # print(n, '시작')
#         for i in range(len(n) - 1):
#             # print(i)
#             if n[i] < n[i + 1]:
#                 # print(n[i], n[i+1])
#                 n.pop(i)
#                 count += 1
#                 break
#     return str(''.join(n))

#########################################################