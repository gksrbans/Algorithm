# -*- conding: utf-8 -*-

'''
Author : gksrbans123@gmail.com
Date : 2020-10-04 // 힝 ^ㅠ^
URL : https://programmers.co.kr/learn/courses/30/lessons/42583
Type : Queue
'''

from collections import deque

def solution(b, w, t):
    time = 0
    q = deque([0]* b, maxlen=b)
    x = deque(t)
    current = 0
    temp = 0

    while t:
        time += 1
        x = q.popleft()
        current -= x

        if t[0] + current > w:
            q.append(0)
        else:
            out_truck = t.pop(0)
            q.append(out_truck)
            current += out_truck

    while current > 0:
        time +=1
        x = q.popleft()
        current -= x

    return time

# Reference : https://assaeunji.github.io/python/2020-05-08-pgtruck/
# 무수한 실패 끝에 구글링함 ㅜ_ㅜ

#################################################
# 첫 번째 코드
# 반복 루프를 어떤걸 기준으로 돌릴지 제대로 결정하지 못했다.

# from collections import deque
#
#
# def solution(b, w, t):
#     Range = len(t)
#     q = deque(maxlen=b)
#
#     flag = True
#     result = []
#     time = 0
#
#     while len(result) != Range:
#         # print(q)
#         time += 1
#
#         if t[0] + sum(q) <= w:
#             q.appendleft(t[0])
#             result.append(t[0])
#             t.pop(0)
#         elif t[0] + sum(q) > w:
#             q.appendleft(0)
#
#         if len(q) >= b:
#             flag = False
#
#     if flag == True:
#         time = time + b
#     elif flag == False:
#         time = time
#
#     return time

#################################################
# 두 번째 실패 코드
# 테스트케이스 5번에서 sum() 자체의 시간 복잡도가 O(N)이라서 시간초과로 실패함
# 실제로 다른사람의 풀이에도 sum()을 써서 풀이한건 테스트케이스를 간당간당하게 통과하거나 실패한 경우가 많았음.
# 트럭의 현재 current 무게를 알 수 있도록 다시함
# 가늠이 잘 안돼서 구글링 했음...

# from collections import deque
#
#
# def solution(b, w, t):
#     time = 0
#     q = deque([0] * b, maxlen=b)
#     x = deque(t)
#
#     while q:
#         time += 1
#         q.popleft()
#         if x:
#             if x[0] + sum(q) <= w:
#                 q.append(x[0])
#                 x.popleft()
#             else:
#                 q.append(0)
#     return time

#################################################
