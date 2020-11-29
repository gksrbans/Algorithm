# -*- conding: utf-8 -*-

'''
Author : gksrbans123@gmail.com
Date : 2020-11-29
URL : https://programmers.co.kr/learn/courses/30/lessons/43165
Type : DFS / BFS
'''

cnt = 0

def DFS(numbers, target, index=0):
    global cnt
    if index < len(numbers): # index 끝까지 안왔다면
        numbers[index] *= 1
        DFS(numbers, target, index+1)

        numbers[index] *= -1
        DFS(numbers, target, index+1)

    elif sum(numbers) == target: #index가 끝까지왔을때 합이 같다면
        cnt += 1

def solution(numbers, target):
    DFS(numbers, target)
    return cnt


answer = 0

######################################################################
# 훨씬 깔끔한 DFS 구현

# def DFS(index, numbers, target, value):
#     global answer
#
#     if (index == len(numbers) and target == value):
#         answer += 1
#     if (index == len(numbers)):
#         return
#
#     DFS(index + 1, numbers, target, value + numbers[index])
#     DFS(index + 1, numbers, target, value - numbers[index])
#
#
# def solution(numbers, target):
#     global answer
#     DFS(0, numbers, target, 0)
#     return answer
######################################################################