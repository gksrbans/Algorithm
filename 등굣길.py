# -*- conding: utf-8 -*-

'''
Author : gksrbans123@gmail.com
Date : 2020-11-25
URL : https://programmers.co.kr/learn/courses/30/lessons/42898
Type : Dynamic Programming
'''

def solution(m, n, puddles):
    # 위쪽과 왼쪽을 계속해서 더해나가면 최단경로에 이른다는 마인드네
    array = [[0 for i in range(m + 1)] for j in range(n + 1)]
    array[1][1] = 1  # 집
    # print(array)

    for i in range(1, n + 1):
        # print(i)
        for j in range(1, m + 1):
            # print(i, j)
            if [j, i] in puddles:
                continue
            if i == 1 and j == 1:
                continue
            array[i][j] = array[i - 1][j] + array[i][j - 1]

    return array[-1][-1] % 1000000007

#################################################################

# 최단경로를 어떻게 설정하느냐를 고민하게 만듬.
# 왼쪽과 위쪽 경로를 더해서 새로운 배열을 계속 더해가서 최종 답을 구한다.
# 맨위와 왼쪽에 '0'을 추가해 indexErr를 방지.
# 생각이 참 중요하다고 깨달았다.