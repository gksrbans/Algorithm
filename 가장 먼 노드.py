# -*- conding: utf-8 -*-

'''
Author : gksrbans123@gmail.com
Date : 2020-12-26
URL : https://programmers.co.kr/learn/courses/30/lessons/49189
Type : Graph
'''

# 인접 행렬 배열을 생성한 뒤에 BFS를 돌린다는 생각을 한다는게 중요함.
# BFS 탐색 시 visit하지 않은 노드 및 자식들 추가.
# 끝까지 진행 후 max값과 비교해 return

from collections import deque


def bfs(v, visited, adj):
    count = 0
    q = deque([[v, count]])

    while q:
        temp = q.popleft()
        v = temp[0]
        count = temp[1]
        if visited[v] == -1:  # 방문하지 않은 노드일 경우
            visited[v] = count
            count += 1

            for i in adj[v]:
                q.append([i, count])


def solution(n, edge):
    answer = 0
    visited = [-1] * (n + 1)

    # 인접행렬 선언
    adj = [[] for _ in range(n + 1)]

    for e in edge:
        x = e[0]
        y = e[1]

        adj[x].append(y)
        adj[y].append(x)

    # print(adj) [[], [3, 2], [3, 1, 4, 5], [6, 4, 2, 1], [3, 2], [2], [3]]

    bfs(1, visited, adj)
    # print(visited)

    for i in visited:
        if i == max(visited):
            answer += 1
    return answer