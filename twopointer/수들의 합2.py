# -*- conding: utf-8 -*-

'''
Author : gksrbans123@gmail.com
Date : 2021-08-31
URL : https://www.acmicpc.net/problem/2003
Type : Two-Pointer
'''

import sys

sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(10 ** 6)

N, M = map(int, input().split())
A = list(map(int, input().split()))

answer = 0
left, right = 0, 0

while right<=len(A) and left<= right: # 오른쪽 커서를 끝까지 탐색하며 왼쪽 커서가 오른쪽 커서를 넘어가지 않는 loop에서 탐색함.
    tmp = sum(A[left:right])

    if tmp < M: # 만약 부분합이 M 보다 작으면 right를 늘린다.
        right += 1
        continue

    elif tmp > M: # 만약 부분합이 M 보다 크면 left를 늘려야함
        left += 1
        continue

    elif tmp == M: # 같으면 왼쪽을 한칸늘려주는게 맞는듯 오른쪽늘려도 상관없는듯
        answer += 1
        left += 1

print(answer)