# -*- conding: utf-8 -*-

'''
Author : gksrbans123@gmail.com
Date : 2021-04-05
URL : https://www.acmicpc.net/problem/17182
Type : ?
'''

import sys

sys.stdin = open('input.txt', 'r')

N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

#print(board)

for k in range(N):
    for i in range(N):
        for j in range(N):
            if i == j: continue
            board[i][j] = min(board[i][j], board[i][k] + board[k][j])


#print(board)

_INF = 1e9
ret = [_INF]
visited = [False] * N
visited[K] = True

def DFS(arr, visited, ret, start_node, cost, planet, N):
    if ret[0] < cost:
        return

    if planet == N:
        ret[0] = min(ret[0], cost)
        return

    for i in range(N):
        if visited[i]: continue
        else:
            visited[i] = True
            DFS(arr, visited, ret, i, cost + board[start_node][i], planet + 1, N)
            #DFS(arr, visited, ret, i, cost + arr[start_node][i], planet + 1, N)
            visited[i] = False

DFS(board, visited, ret, K, 0, 1, N)
print(ret[0])
