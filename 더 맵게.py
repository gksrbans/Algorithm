# -*- conding: utf-8 -*-

'''
Author : gksrbans123@gmail.com
Date : 2020-10-12 // 힙 ㅡ 합
URL : https://programmers.co.kr/learn/courses/30/lessons/42626
Type : Heap
'''

import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    count = 0

    while scoville[0] < K:
        try:
            heapq.heappush(scoville, heapq.heappop(scoville) + (heapq.heappop(scoville) * 2))
            count += 1
        except:
            return -1

        #print(scoville, count)
    return count

########################################################

#첫 번째 풀이는 함수를 따로만들어서 heapq 모듈을 사용해 구현

# import heapq
#
# loop = 0
# Range = 0
#
#
# def test(scoville, K):
#     global loop, Range
#     loop += 1
#
#     heapq.heapify(scoville)
#     first = heapq.heappop(scoville)
#     if first > K:
#         return -1
#
#     second = heapq.heappop(scoville)
#     if second > K:
#         return -1
#
#     temp = first + (second * 2)
#     heapq.heappush(scoville, temp)
#
#     if temp >= K:
#         return -1
#
#     if loop == Range - 1 and temp < K:
#         return -1
#     return scoville
#
#
# def solution(scoville, K):
#     global Range
#     Range = len(scoville)
#     count = 0
#     # print(Range, scoville, count)
#     while (len(scoville) > 1):
#
#         count += 1
#         ans = test(scoville, K)
#         # print(Range, scoville, count, ans)
#
#         if ans == -1:
#             break
#     return count