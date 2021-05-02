# -*- conding: utf-8 -*-

'''
Author : gksrbans123@gmail.com
Date : 2021-05-02
URL : https://www.acmicpc.net/problem/2583
Type : DFS
'''

import sys
import copy
sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(10 ** 6)

M, N, K = map(int, input().split())
board = [[0] * N for _ in range(M)]
visited = [[0] * N for _ in range(M)]
nums = 0 # 영역
num = 0 # 블록 갯수
result = []

# 4방향 써치
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

for i in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for a in range(x1, x2):
        for b in range(y1, y2):
            board[b][a] = 1

#print(board)

def dfs(row, col):
    global num
    visited[row][col] = 1
    num += 1

    for i in range(4):
        ny = row + dy[i]
        nx = col + dx[i]
        if 0<= ny < M and 0<= nx < N:
            if board[ny][nx] == 0 and visited[ny][nx] == 0:
                dfs(ny, nx)

for i in range(M):
    for j in range(N):
        if board[i][j] == 0 and visited[i][j] == 0:
            dfs(i, j)
            result.append(num)
            nums += 1
            num = 0

print(nums)
print(*sorted(result))