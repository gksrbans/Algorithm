# -*- conding: utf-8 -*-

'''
Author : gksrbans123@gmail.com
Date : 2020-10-11 // 힝 ^ㅠ^
URL : https://programmers.co.kr/learn/courses/30/lessons/42587
Type : Queue
'''

#from collections import deque
#q = deque([])

# 1. 배열 인덱스를 생성해 튜플로 붙힌다.
# 2. 튜플리스트를 집어넣으면 boolean 값을 출력하는 함수를 만든다.
# 3. 함수가 정렬이 될때 까지 while문을 돌면서 정렬한다.
# 4. location와 index가 일치하는 값을 출력한다.
# ★ 로직상 어디가 문제가 있는지 모르겠다. (테스트 케이스 반정도 통과)

def isDescending(tuple1):
    isDescending = True
    row = []
    for i in range(len(tuple1)):
        row.append(tuple1[i][1])

    for i in range(1, len(row)):
        if (row[i] > row[i - 1]):
            isDescending = False

    if (isDescending):
        return True
    else:
        return False


def solution(p, l):
    index = []
    k = 0

    for i in range(len(p)):
        index.append(k)
        k += 1
        # print(index)

    x = [x for x in zip(index, p)]

    while (isDescending(x) == False):
        flag = False
        for i in range(len(x)):
            for j in range(i + 1, len(x)):
                if x[i][1] < x[j][1]:
                    x.append(x[i])
                    x.pop(i)
                    flag = True
                    break
                if flag == True:
                    break

    for i in range(len(x)):
        if x[i][0] == l:
            return i + 1

###################################################

# 다른사람 풀이
# 나와 생각이 거의 비슷했는데 테스트를 통과 했음.
# 어떤 테스트케이스가 실패하는지 파악 X

# def solution(priorities, location):
#     pi_list = [(p, i) for i, p in enumerate(priorities)]
#     waiting_q = []
#
#     while pi_list:
#         pi = pi_list.pop(0)
#         priority = pi[0]
#         p_list = [priority for priority, idx in pi_list]
#         if p_list:
#             max_p = max(p_list)
#
#         if priority >= max_p:
#             waiting_q.append(pi)
#         else:
#             pi_list.append(pi)
#         for i, item in enumerate(waiting_q):
#             item[1] == location:
#             return i + 1

# https://itholic.github.io/kata-printer/