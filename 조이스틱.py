# -*- conding: utf-8 -*-

'''
Author : gksrbans123@gmail.com
Date : 2020-11-01
URL : https://programmers.co.kr/learn/courses/30/lessons/42860
Type : Greedy
'''
import string


def solution(name):
    answer = []
    result = 0
    temp = 0

    upper = list(string.ascii_uppercase)
    upper_reverse = sorted(string.ascii_uppercase, reverse=True)
    upper_reverse.pop()
    upper_reverse.insert(0, 'A')

    for i in range(len(name)):
        if upper.index(name[i]) <= upper_reverse.index(name[i]):
            answer.append(upper.index(name[i]))
        else:
            answer.append(upper_reverse.index(name[i]))
        print(answer)

    while True:
        result += answer[temp]
        answer[temp] = 0

        if sum(answer) == 0:
            break

        left, right = (1, 1)

        while answer[temp - left] <= 0:
            left += 1

        while answer[temp + right] <= 0:
            right += 1

        result += left if left < right else right
        temp += - left if left < right else right

    return result

####################################################################

# 조이스틱을 상,하로 움직이는 경우와 좌,우로 움직이는 경우를 나누어서 코딩
# 좌,우로 움직이는 부분에서 처음에 왼쪽에서 오른쪽으로 진행하는 경우만 생각해서 TC11번 실패.
# 좌우 비교하는 부분이 있어야 됨. 왜 레벨 2인지 모르겠음 어렵누


# def solution(name):
#     upper = list(string.ascii_uppercase)
#     upper_reverse = sorted(string.ascii_uppercase, reverse=True)
#     upper_reverse.pop()
#     upper_reverse.insert(0, 'A')
#
#     answer = 0
#     flag = True
#
#     for i in range(len(name)):
#         if upper.index(name[i]) <= upper_reverse.index(name[i]):
#             answer += upper.index(name[i])
#         else:
#             answer += upper_reverse.index(name[i])
#         # print(answer)
#     answer += len(name) - 1
#
#     for i in range(1, len(name)):
#         answer -= 1
#         if name[i] != 'A':
#             flag = False
#             break
#
#     return answer + 1
