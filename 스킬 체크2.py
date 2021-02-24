# -*- conding: utf-8 -*-

'''
Author : gksrbans123@gmail.com
Date : 2021-02-24
URL : https://programmers.co.kr/skill_checks/251853
Type : 스킬을 체크해보자
'''

import numpy as np


def solution(arr1, arr2):
    answer = []

    a = np.array(arr1)
    b = np.array(arr2)
    c = np.dot(a, b)

    for i in range(len(c)):
        answer.append(c[i].tolist())

    return answer