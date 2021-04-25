# -*- conding: utf-8 -*-

'''
Author : gksrbans123@gmail.com
Date : 2021-04-25
URL : https://www.acmicpc.net/problem/2606
Type : DFS
'''
import sys

sys.stdin = open("input.txt", "r")
N = int(input())
M = int(input())
board = [[0] * (N+1) for _ in range(N+1)]

for _ in range(M):
    start, end = map(int, input().split())
    board[start][end] = 1
    board[end][start] = 1


def dfs(root, visited):
    visited += [root]
    for i in range(len(board[root])):
        if board[root][i] == 1 and i not in visited:
            dfs(i, visited)
    return visited


# 1 root 노드 제외하고 출력
print(len(dfs(1, [])) - 1)
