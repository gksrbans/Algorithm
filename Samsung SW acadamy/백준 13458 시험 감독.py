# -*- conding: utf-8 -*-

'''
Author : gksrbans123@gmail.com
Date : 2021-04-04
URL : https://www.acmicpc.net/problem/13458
Type : ?
'''

# 총 감독관이 꼭 들어가야하는지 명시가 안되어있긴 한데
# 아무튼 맨처음에 총감독관 빼고 시작함
# 그리고 부감독관 고려해서 답을 찾는데 나머지가 0이 아닐경우에 한명더 필요하므로 한명더 추가함.


import sys
import math

sys.stdin = open("input.txt", "r")

N = int(input())
#print(N)
A = list(map(int, input().split()))
#print(A)
B, C = input().split()
B, C = int(B), int(C)
#print(B, C)

sum = 0


for i in range(N):
    if A[i] > 0:
        A[i] = A[i] - B
        sum += 1

    if A[i] > 0 :
        sum += int(A[i] / C)
        if A[i] % C != 0:
            sum += 1

print(sum)