# -*- conding: utf-8 -*-

'''
Author : gksrbans123@gmail.com
Date : 2020-11-02
URL : https://programmers.co.kr/learn/courses/30/lessons/42885
Type : Greedy
'''

from collections import deque
# people = [70, 80, 50]
# limit = 100
# limit에 최대한으로 묶어서 보트에 태울려면 가장 작은 수와 가장 큰 수를 비교하는게 맞음.

def solution(people, limit):
    people.sort()
    q = deque(people)
    count = 0
    while q:
        if len(q) == 1:
            count += 1
            break

        if q[0] + q[-1] > limit:
            q.pop()
            count += 1
        else:
            q.popleft()
            q.pop()
            count += 1
    return count


########################################################
# 실제로 원소를 pop하지 않고 커서 변수를 따로 선언해서 원래 배열을 훼손하지 않고 푸는것이 가능함.

# people.sort()
# q = deque(people)
# count = 0
# start_cursor = 0
# end_cursor = len(q) - 1
# while start_cursor <= end_cursor:
#     if (q[start_cursor] + q[end_cursor]) > limit:
#         end_cursor -= 1
#
#     else:
#         start_cursor += 1
#         end_cursor -= 1
#     count += 1
#
# print(count)
########################################################



