# -*- conding: utf-8 -*-

'''
Author : gksrbans123@gmail.com
Date : 2021-04-27
URL : https://www.acmicpc.net/problem/11724
Type : DFS
'''

import sys

sys.setrecursionlimit(10000)
sys.stdin=open('input.txt','r')

def dfs(v):
    visited[v] = True
    for e in adj[v]:
        if visited[e] == 0:
            dfs(e)


N, M = map(int, sys.stdin.readline().split())
adj = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
count = 0

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    adj[u].append(v)
    adj[v].append(u)

for j in range(1, N + 1):
    if visited[j] == 0:
        dfs(j)
        count += 1

print(count)

