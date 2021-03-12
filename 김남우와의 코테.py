# -*- conding: utf-8 -*-

'''
Author : gksrbans123@gmail.com
Date : 2021-03-12
URL : https://programmers.co.kr/learn/courses/30/lessons/42888
Type : 오픈채팅방
'''

import collections


def solution(record):
    answer = []
    deq = collections.deque()
    dict = collections.defaultdict()

    for i in record:
        act = i.split(" ")[0]
        user = i.split(" ")[1]
        if act == "Leave":
            pass
        else:
            nickname = i.split(" ")[-1]
            dict[user] = nickname

    for i in record:
        act = i.split(" ")[0]
        user = i.split(" ")[1]
        nickname = dict[user]

        if act == "Enter":
            temp = "{nickname}님이 들어왔습니다.".format(nickname=nickname)
            answer.append(temp)

        elif act == "Leave":
            temp = "{nickname}님이 나갔습니다.".format(nickname=nickname)
            answer.append(temp)

    return answer



