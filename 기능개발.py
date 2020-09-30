# -*- conding: utf-8 -*-

'''
Author : gksrbans123@gmail.com
Date : 2020-09-30 // 즐거운 추석 ^ㅠ^
URL : https://programmers.co.kr/learn/courses/30/lessons/42586
Type : Queue
'''

import math
#from collections import deque
from collections import Counter

def solution(p, s):
    answer = []
    stack = 0
    count = 0
    result = []

    #q = deque([])
    for i in range(len(p)):
        p[i] = 100 - p[i]
        p[i] = math.ceil(p[i] / s[i])

    for i in range(len(p)):
        count += 1
        if stack < p[i]:
            stack = p[i]

            key = p[i]
        answer.append(key)

    x = Counter(answer)
    x = sorted(x.items(), key=lambda x:x[0])

    for i in x:
        result.append(i[1])
    return result


#####################################################

# 다른 사람의 풀이.
# 세상에 코딩을 잘하는 사람이 얼마나 많은지 깨달았다.
# time 변수를 저런식으로 줘서 문제를 풀다니... 아주 직관적이고 좋은 코드인거 같다.

# def solution(progresses, speeds):
#     answer = []
#     time = 0
#     count = 0
#     while len(progresses)> 0:
#         if (progresses[0] + time*speeds[0]) >= 100:
#             progresses.pop(0)
#             speeds.pop(0)
#             count += 1
#         else:
#             if count > 0:
#                 answer.append(count)
#                 count = 0
#             time += 1
#     answer.append(count)
#     return answer

#####################################################