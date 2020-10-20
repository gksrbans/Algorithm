# -*- conding: utf-8 -*-

'''
Author : gksrbans123@gmail.com
Date : 2020-10-20
URL : https://programmers.co.kr/learn/courses/30/lessons/42747
Type : Sort
'''

def solution(citations):
    temp = max(citations)
    answer = []

    for i in range(temp, 0, -1):
        c2 = []
        c3 = []

        for j in range(len(citations)):
            #print(citations[j], 'j임')
            if citations[j] >= i:
                c2.append(citations[j])
            elif citations[j] <= i:
                c3.append(citations[j])

        if len(c2) >= i >= len(c3):
            answer.append(i)
    if answer:
        return max(answer)
    else:
        return 0

######################################################

# 다른 사람 풀이.
# max나 min 따위를 쓰지않고 너무 멋있다;

# def solution(citations):
#     citations = sorted(citations)
#     l = len(citations)
#     for i in range(l):
#         if citations[i] >= l-i:
#             return l-i
#     return 0

######################################################