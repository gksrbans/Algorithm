# -*- conding: utf-8 -*-

'''
Author : gksrbans123@gmail.com
Date : 2020-10-23
URL : https://programmers.co.kr/learn/courses/30/lessons/42840
Type : Exhaustive Search
'''


def solution(answers):
    pattern1 = [1, 2, 3, 4, 5]
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    count1 = 0
    count2 = 0
    count3 = 0

    temp = []
    for i in range(len(answers)):
        if answers[i] == pattern1[i % 5]:
            count1 += 1
        if answers[i] == pattern2[i % 8]:
            count2 += 1
        if answers[i] == pattern3[i % 10]:
            count3 += 1

    maxnum = max([count1, count2, count3])

    if count1 == maxnum:
        temp.append(1)
    if count2 == maxnum:
        temp.append(2)
    if count3 == maxnum:
        temp.append(3)

    return temp
