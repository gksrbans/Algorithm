# -*- conding: utf-8 -*-

'''
Author : gksrbans123@gmail.com
Date : 2020-10-15 // (재도전)
URL : https://programmers.co.kr/learn/courses/30/lessons/42627
Type : Heap
'''


# 다시할거임 아ㅏㅏㅏ나ㅏㅏㅏㅏ

import heapq

def solution(jobs):
    jobs.sort()
    h = []
    index = [0]
    index2 = [0]

    for i in jobs:
        heapq.heappush(h, (i[1], i[0]))

    for i in range(len(h)):
        temp = heapq.heappop(h)
        print(temp)
        index.append(index[-1] + temp[0])

        if index[-1] > temp[1]:
            index2.append(temp[1])
        else:
            index2.append(0)
    for i in range(len(index)):
        index[i] = index[i] - index2[i]

    answer = sum(index) // len(jobs)
    return answer