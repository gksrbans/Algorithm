# -*- conding: utf-8 -*-

'''
Author : gksrbans123@gmail.com
Date : 2020-10-17
URL : https://programmers.co.kr/learn/courses/30/lessons/42748
Type : Sort
'''


def solution(array, commands):
    ans = []
    for i in commands:
        start = i[0] - 1
        end = i[1]
        search = i[2] - 1

        answer = sorted(array[start:end])
        ans.append(answer[search])

    return ans