# -*- conding: utf-8 -*-

'''
Author : gksrbans123@gmail.com
Date : 2021-01-20
URL : https://programmers.co.kr/learn/courses/30/lessons/17676
Type : 카카오 가고 싶다...
'''


def checknum(time, result):
    start_time = time
    end_time = time + 1000
    count = 0

    for i in result:
        if i[1] >= start_time and i[0] < end_time:
            count += 1
    return count


def solution(lines):
    result = []
    compare = 1

    for line in lines:
        year, end_time, delay = line.split(' ')
        delay = delay[:-1]
        end_time = end_time.split(':')
        delay = float(delay.replace('s', '')) * 1000
        # print(delay)
        end = (int(end_time[0]) * 3600 + int(end_time[1]) * 60 + float(end_time[2])) * 1000  # 밀리세컨드로 변환
        start_time = end - delay + 1

        result.append([start_time, end])

        # print(result)

    for i in result:
        compare = max(compare, checknum(i[0], result), checknum(i[1], result))

    return compare
