# -*- conding: utf-8 -*-

'''
Author : gksrbans123@gmail.com
Date : 2020-12-26
URL : https://programmers.co.kr/learn/courses/30/lessons/49189
Type : Graph
'''

# DFS / BFS / 그래프에 들어와서 생각하는게 많이 어려워졌음
# Hash를 이용한 풀이를 참조했음(https://velog.io/@tjdud0123/%EC%88%9C%EC%9C%84-python)
# 이긴사람과 진사람의 set을 만들어서 길이가지고 비교.
# 비트연산자를 이용해 완성시킴 ( update로도 같은 효과 볼수 있음 )
# 최종 길이가 n-1 과 똑같은 놈들만 return

from collections import defaultdict

def solution(n, results):
    answer = 0
    wins = defaultdict(set)
    loses = defaultdict(set)

    for a, b in results:
        wins[a].add(b)
        loses[b].add(a)

    for i in range(1, n+1):
        for loser in wins[i]:
            loses[loser] |= loses[i]
        for winner in loses[i]:
            wins[winner] |= wins[i]

    for i in range(1, n+1):
        if len(wins[i]) + len(loses[i]) == n - 1:
            answer += 1

    return answer