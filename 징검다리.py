# -*- conding: utf-8 -*-

'''
Author : gksrbans123@gmail.com
Date : 2020-12-20
URL : https://programmers.co.kr/learn/courses/30/lessons/43236
Type : Binary Search
'''

# 이분탐색의 기준을 구하고자 하는 최솟값을 기준으로 함
# 돌덩이 갯수를 더많이 뺏으면 right를 당기고 그외에는 left를 증가시킴
def solution(distance, rocks, n):
    answer = 0
    left = 0
    right = distance
    rocks.sort()

    while left <= right:
        mid = (left + right) // 2
        pre_rock = 0
        num_of_rock = 0
        m_min = 1000000001

        for rock in rocks:
            if rock - pre_rock < mid:
                num_of_rock += 1
            else:
                m_min = min(rock - pre_rock, m_min)
                pre_rock = rock

        if num_of_rock > n:
            right = mid - 1
        else:
            answer = m_min
            left = mid + 1

    return answer