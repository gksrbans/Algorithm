# -*- conding: utf-8 -*-

'''
Author : gksrbans123@gmail.com
Date : 2021-05-02
URL : https://www.acmicpc.net/problem/10026
Type : DFS
'''

import sys
import copy

sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(10 ** 6)

N = int(input())
board = [list(input()) for _ in range(N)]
board2 = []
visited = [[0] * N for _ in range(N)]
visited2 = [[0] * N for _ in range(N)]


resion = 0  # 적록색약
resion2 = 0  # 적록색약 아닌 사람.

# print(board)
# print(visited)
# 색맹을 위한 보드2 선언
for items in board:
    temp = []
    for item in items:
        if item == 'G':
            temp.append('R')
        else: temp.append(item)
    board2.append(temp)

#print(board)
#print(board2)


# 4방향 써치
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def dfs(row, col):
    visited[row][col] = 1

    for i in range(4):
        ny = row + dy[i]
        nx = col + dx[i]

        if 0<= ny < N and 0 <= nx < N:
            if board[ny][nx] == 'R' and visited[ny][nx] == 0:
                dfs(ny, nx)


def dfs2(row, col):
    visited2[row][col] = 1

    for i in range(4):
        ny = row + dy[i]
        nx = col + dx[i]

        if 0<= ny < N and 0 <= nx < N:
            if board2[ny][nx] == 'R' and visited2[ny][nx] == 0:
                dfs2(ny, nx)

def dfs_g(row, col):
    visited[row][col] = 1

    for i in range(4):
        ny = row + dy[i]
        nx = col + dx[i]

        if 0<= ny < N and 0 <= nx < N:
            if board[ny][nx] == 'G' and visited[ny][nx] == 0:
                dfs_g(ny, nx)

def dfs_b(row, col):
    visited[row][col] = 1
    for i in range(4):
        ny = row + dy[i]
        nx = col + dx[i]

        if 0<= ny < N and 0 <= nx < N:
            if board[ny][nx] == 'B' and visited[ny][nx] == 0:
                dfs_b(ny, nx)

def dfs_b2(row, col):
    visited2[row][col] = 1
    for i in range(4):
        ny = row + dy[i]
        nx = col + dx[i]

        if 0<= ny < N and 0 <= nx < N:
            if board2[ny][nx] == 'B' and visited2[ny][nx] == 0:
                dfs_b2(ny, nx)


def solve():
    global resion, resion2
    for i in range(N):
        for j in range(N):
            if board[i][j] == 'R' and visited[i][j] == 0:
                dfs(i, j)
                resion += 1
            if board[i][j] == 'G' and visited[i][j] == 0:
                dfs_g(i, j)
                resion += 1
            if board[i][j] == 'B' and visited[i][j] == 0:
                dfs_b(i,j)
                resion += 1

            if board2[i][j] == 'R' and visited2[i][j] == 0:
                dfs2(i, j)
                resion2 += 1

            if board2[i][j] == 'B' and visited2[i][j] == 0:
                dfs_b2(i,j)
                resion2 += 1

solve()

print(resion, resion2)
