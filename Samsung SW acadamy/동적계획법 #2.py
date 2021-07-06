# -*- conding: utf-8 -*-

'''
Author : gksrbans123@gmail.com
Date : 2021-07-06
URL : https://programmers.co.kr/learn/courses/30/lessons/42898
Type : DP
'''

triangle = 	[[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]

for i in range(1, len(triangle)): # 1,2,3,4
    for j in range(i+1): # 인자가 한개씩 더많으니까 +1
        if j == 0: # 가장 맨쪽 테두리 이면 위에꺼랑 더햄
            triangle[i][j] += triangle[i-1][j]
        elif i == j:
            triangle[i][j] += triangle[i-1][j-1]
        else:
            triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j-1])

print(max(triangle[-1]))
