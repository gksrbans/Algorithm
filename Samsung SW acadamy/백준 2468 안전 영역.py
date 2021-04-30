# -*- conding: utf-8 -*-

'''
Author : gksrbans123@gmail.com
Date : 2021-04-30
URL : https://www.acmicpc.net/problem/2468
Type : DFS
'''

import sys
import copy
sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(10 ** 6)

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
visited2 = [[0] * N for _ in range(N)]

#print(max(max(board)))


dy = [-1, 1, 0 ,0]
dx = [0, 0, -1, 1]
result = [] # 결과 값 반환

def dfs(row, col, _cnt):
    visited[row][col] = 1
    #print('들어옴')
    for i in range(4):
        ny = row + dy[i]
        nx = col + dx[i]
        if 0<= ny < N and 0<= nx < N:
            if board[ny][nx] > limit and visited[ny][nx] == 0:
                dfs(ny, nx, _cnt)

#print(board)

for limit in range(max(max(board))):
    visited = copy.deepcopy(visited2)
    cnt = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] > limit and visited[i][j] == 0:
                #print('진입')
                dfs(i, j, cnt)
                cnt += 1
    result.append(cnt)

print(max(result))


