# -*- conding: utf-8 -*-

'''
Author : gksrbans123@gmail.com
Date : 2020-12-13
URL : https://programmers.co.kr/learn/courses/30/lessons/43238
Type : Binary Search
'''

# times를 오름차순 sort()
# 각 time마다 심사자가 들어감. n이 0이 될때까지 for문 ?


def solution(n, times):
    length = len(times)
    left = 1
    right = (length + 1) * max(times)

    while left <= right:
        mid = (left + right) // 2
        count = 0

        # print(mid)

        for time in times:
            count += mid // time
            if count >= n:
                break

        if count >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer
