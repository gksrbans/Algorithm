# -*- conding: utf-8 -*-

'''
Author : gksrbans123@gmail.com
Date : 2021-07-06
URL : https://programmers.co.kr/learn/courses/30/lessons/42898
Type : DP
'''

m, n, puddles = 4, 3, [[2, 2]]


array = [[0 for i in range(m+1)] for j in range(n+1)]
array[1][1] = 1
print(array)

for i in range(n+1):
    for j in range(m+1):
        if i== 1 and j== 1:
            continue
        array[i][j] = array[i-1][j] + array[i][j-1]

print(array)
print(array[-1][-1] % 1000000007)
