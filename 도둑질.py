# -*- conding: utf-8 -*-

'''
Author : gksrbans123@gmail.com
Date : 2020-11-28
URL : https://programmers.co.kr/learn/courses/30/lessons/42897
Type : Dynamic Programming
'''

# 집이 한 개일때부터 2개, 3개 하나씩 경우의 수를 늘려가면서 생각하기
# 집 좌우로는 돈을 훔칠수 없으니까 i-2, i값을 합친것과, 중간값중에 max값을 리턴하자
# Referer: https://velog.io/@imacoolgirlyo/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%8F%84%EB%91%91%EC%A7%88-%ED%8C%8C%EC%9D%B4%EC%8D%AC

def solution(money):
    dp1 = [0] * len(money)
    #print(dp1)

    dp1[0] = money[0]
    dp1[1] = max(money[0], money[1])

    for i in range(2, len(money)-1):
        #print(i)
        dp1[i] = max(dp1[i-1], money[i] + dp1[i-2])

    dp2 = [0] * len(money)
    dp2[0] = 0
    dp2[1] = money[1]

    for i in range(2, len(money)):
        dp2[i] = max(dp2[i-1], money[i]+dp2[i-2])

    #print(dp1, dp2)
    return max(max(dp1), max(dp2))