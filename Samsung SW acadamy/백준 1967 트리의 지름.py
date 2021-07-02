# -*- conding: utf-8 -*-

'''
Author : gksrbans123@gmail.com
Date : 2021-07-02
URL : https://www.acmicpc.net/problem/1967
Type : Tree DP
'''

import sys
from collections import deque

sys.stdin = open("input.txt", "r")
sys.setrecursionlimit(100000)

def dfs(start, graph, weight, ck):
    if ck == 1:
        weight[1] = 0
    #print(start, 'start임')


    for _node, w in graph[start]:
        #print(_node)
        #print(weight[_node])
        if weight[_node] == 0:
            weight[_node] = weight[start] + w
            dfs(_node, graph, weight, ck)

T = int(input())
graph = [[] for _ in range(T+1)]

for i in range(T-1):
    parent, child, weight = map(int, input().split())
    graph[parent].append((child, weight))
    graph[child].append((parent, weight))
#print(graph)

#print(graph)
weight1 = [0 for _ in range(T+1)]
dfs(1,graph,weight1, 1)
#print(weight1)

start_node = weight1.index(max(weight1))
#print(start_node)
weight2 = [ 0 for _ in range(T+1)]
dfs(start_node, graph, weight2, 2)
weight2.pop(start_node)

print(max(weight2))