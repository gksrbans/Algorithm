# -*- conding: utf-8 -*-

'''
Author : gksrbans123@gmail.com
Date : 2020-09-30 // 즐거운 추석 ^ㅠ^
URL : https://programmers.co.kr/learn/courses/30/lessons/42584
Type : Stack
'''


class stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        return not self.items


def solution(prices):
    result = []
    stk = stack()

    for i in range(len(prices)):
        stk.push(prices[i])
        count = 0
        for j in range(i + 1, len(prices)):

            # print(prices[i], prices[j])
            if prices[i] <= prices[j]:
                count += 1

            elif prices[i] > prices[j]:
                count += 1
                stk.pop()
                break
        result.append(count)
    return result

###############################################

# 첫 번째 실패코드
# 예외처리에 대한 부분이 부족하여 실패 발생.
# 스택에 대한 개념정리 문제

# class stack:
#     def __init__(self):
#         self.items = []
#
#     def push(self, item):
#         self.items.append(item)
#
#     def pop(self):
#         return self.items.pop()
#
#     def isEmpty(self):
#         return not self.items
#
#
# def solution(prices):
#     result = []
#     stk = stack()
#
#     for i in range(len(prices)):
#         count = 0
#         stk.push(prices[i])
#
#         for j in range(i + 1, len(prices)):
#             count += 1
#             # print(prices[i], prices[j], count)
#             if prices[i] > prices[j]:
#                 count -= 1
#                 stk.pop()
#         result.append(count)
#     return result

###############################################