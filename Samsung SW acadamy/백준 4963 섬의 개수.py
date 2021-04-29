# -*- conding: utf-8 -*-

'''
Author : gksrbans123@gmail.com
Date : 2021-04-29
URL : https://www.acmicpc.net/problem/4963
Type : DFS
'''

import sys

sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(10000)

# 대각
dy = [-1, 1, 0, 0, 1, 1, -1, -1]
dx = [0, 0, -1, 1, 1, -1, 1, -1]


def dfs(row, col):
    visited[row][col] = 1
    for i in range(8):

        # 인접
        ny = row + dy[i]
        nx = col + dx[i]

        if 0<= ny < h and 0 <= nx < w:
            if board[ny][nx] == 1 and visited[ny][nx] == 0:
                dfs(ny, nx)


try:
    while 1:
        w, h = map(int, input().split())
        if w == 0 and h == 0:
            break
        board = [list(map(int, input().split())) for _ in range(h)]
        visited = [[0] * (w) for _ in range(h)]
        nums = 0

        for i in range(h):
            for j in range(w):
                if board[i][j] == 1 and visited[i][j] == 0:
                    nums += 1
                    dfs(i, j)

        print(nums)

except:
    pass
