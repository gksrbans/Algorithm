# -*- conding: utf-8 -*-

'''
Author : gksrbans123@gmail.com
Date : 2021-04-17
URL : https://www.acmicpc.net/problem/14889
Type : ?
'''

import sys

sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(100001)

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [0 for _ in range(N)]
answer = int(1e9)


def dfs(idx, cnt):
    global answer
    if cnt == N//2:
        start, link = 0, 0

        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]: # 방문하지 않았으면
                    start += board[i][j]
                elif not visited[i] and not visited[j]: # 방문했으면 연결시켜줌
                    link += board[i][j]

        answer = min(answer, abs(start - link))
    for i in range(idx, N):
        if visited[i]: continue

        visited[i] = 1
        dfs(i+1, cnt + 1)
        visited[i] = 0

dfs(0,0)
print(answer)