# -*- conding: utf-8 -*-

'''
Author : gksrbans123@gmail.com
Date : 2021-04-26
URL : https://www.acmicpc.net/problem/1012
Type : DFS
'''


import sys
sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(10000)

# 상 하 좌 우 변수
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def dfs(row, col, _cnt):
    visited[row][col] = _cnt

    for i in range(4):
        ny = row + dy[i]
        nx = col + dx[i]

        if 0 <= ny < N and 0<= nx < M: #보드 안에 있다면,
            if board[ny][nx] == 1 and visited[ny][nx] == 0: # 새로운 좌표에 집이 있고, 방문하지 않았따면 dfs 호출
                dfs(ny, nx, _cnt)


T = int(input())
#print(T)

for _ in range(T):
    M, N, K = map(int, input().split())
    board = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    cnt = 0

    for _ in range(K):
        X, Y = map(int, input().split())
        board[Y][X] = 1 # 좌표는 row, col 반대;

    for i in range(N):
        for j in range(M):
            if board[i][j] == 1 and visited[i][j] == 0:
                cnt += 1
                dfs(i, j, cnt)
                #print(visited)

    print(cnt)






