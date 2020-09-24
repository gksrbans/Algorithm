# -*- conding: utf-8 -*-

'''
Author : gksrbans123@gmail.com
Date : 2020-09-24
URL : https://programmers.co.kr/learn/courses/30/lessons/42576
Type : Hash
'''


# def solution(participant, completion):
#     answer = ''
#     for i in range(len(completion)):
#         participant.remove(completion[i])
#
#     for i in range(len(participant)):
#         answer += participant[i]
#
#     return answer
# 시간초과 실패 코드. Hash의 특성을 전혀 살리지 못했다.

def solution(participant, completion):
    participant.sort()
    completion.sort()

    x = zip(participant, completion)
    for i, v in x:
        if i != v:
            return i
    return participant[-1]
# 이 풀이는 문제 조건에 '단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.' 라는 조건이 있어서 이런 풀이가 가능했다.
# 이렇게 sort에서 푸는데에는 한계가 있다고 생각해서 다른 풀이를 찾아보았다.


# import collections
#
# def solution(participant, completion):
#     answer = collections.Counter(participant) - collections.Counter(completion)
#     return list((answer.keys()))[0]

# collections 모듈에 대해서는 알고있었으나 Counter 사용해서 서로 뺄셈이 된다는건 처음알았다... 놀라웠다.