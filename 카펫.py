# -*- conding: utf-8 -*-

'''
Author : gksrbans123@gmail.com
Date : 2020-10-24
URL : https://programmers.co.kr/learn/courses/30/lessons/42839
Type : Exhaustive Search
'''

def solution(brown, yellow):
    for i in range(1, yellow + 1):
        if yellow % i == 0:
            temp = [yellow//i, i]
            if temp[0] * 2 + i * 2 + 4 == brown:
                return [yellow//i + 2, i + 2]

##############################################################

# 수학적인 걸 잘 생각하면 더 쉽고 빠르게 풀 수 있었을거 같다
# 약수의 조합에서 가운데 원소를 답으로 제출하면 풀릴거라고 생각했으나, 테스트케이스 4,6,7번이 실패한다.
# 반례를 생각해보니 그런 예가 존재해서 다른 방식으로 생각해야 했다

# 첫 번째 제출 코드

# def solution(brown, yellow):
#     sum = brown + yellow
#     arr = []
#     answer = []
#     for i in range(1, sum + 1):
#         #print(i)
#         if sum % i == 0:
#             arr.append(i)
#     if (yellow+2) * 2 + 2 == brown:
#         answer.append(yellow + 2)
#         answer.append(3)
#
#     elif len(arr)%2 == 0:
#         answer.append(arr[len(arr) // 2])
#         answer.append(arr[len(arr) // 2 - 1])
#     else:
#         answer.append(arr[len(arr) // 2])
#         answer.append(arr[len(arr) // 2])
#     return answer