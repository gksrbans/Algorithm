# -*- conding: utf-8 -*-

'''
Author : gksrbans123@gmail.com
Date : 2020-10-24
URL : https://programmers.co.kr/learn/courses/30/lessons/42839
Type : Exhaustive Search
'''

import itertools

def thtn(num):
    if num <= 1:
        return False
    if num == 2 or num == 3:
        return True
    for i in range(2, num):
        if num % i == 0:
            return False
        else:
            pass
    return True

def solution(numbers):
    array = list(numbers)
    Range = len(array) + 1
    temp = []
    answer = set()
    submit = 0

    for i in range(1, Range):
        temp.append(list(map(''.join, itertools.permutations(array, i))))


    for i in range(len(temp)):
        for j in temp[i]:
            answer.add(int(j))

    for i in answer:
        if thtn(i):
            submit += 1

    return submit

###########################################################

# 기존에 permutations으로 만든 순열 들에 대해서 set()을 이용해 중복제거
# set() 메서드의 add에 대해서 숙지할 수 있게 되었다.