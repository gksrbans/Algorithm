# -*- conding: utf-8 -*-

'''
Author : gksrbans123@gmail.com
Date : 2020-10-25
URL : https://programmers.co.kr/learn/courses/30/lessons/42862
Type : Greedy
'''

def solution(n, lost, reserve):
    arr = [1] * n

    # 이렇게 for문을 돌리면 체육복을 여분을 가져오고 잃어버린 경우의 수가 포함이 안됨
    # 생각지도 못한거에 시간을 많이 잡아먹었었다..

    # for i in range(n):
    #     if i+1 in lost:
    #         arr[i] -= 1
    #     elif i+1 in reserve:
    #         arr[i] += 1
    #     else:
    #         arr[i]
    # print(arr)

    for i in range(n):
        if i+1 in reserve:
            arr[i] = 2

    for i in range(n):
        if i+1 in lost:
            arr[i] = arr[i] - 1

    for i, v in enumerate(arr):
        #print(i, v)
        if i>0 and v==0 and arr[i-1] == 2:
            arr[i] = 1
            arr[i-1] = 1
        elif i<n-1 and v==0 and arr[i+1] ==2:
            arr[i] = 1
            arr[i+1] = 1
    return n-arr.count(0)






