# -*- conding: utf-8 -*-

'''
Author : gksrbans123@gmail.com
Date : 2021-02-13
URL : https://programmers.co.kr/learn/courses/30/lessons/72413
Type : 2021 카카오 kakakao
'''
import heapq

INF = float('inf')
graph = [[]]


def Progress(n, fares):
    global graph
    graph = [[] for i in range(n+1)]

    for fare in fares:
        src, dst, cost = fare
        graph[src].append([dst, cost])
        graph[dst].append([src, cost])


def dijkstra(src, dst):
    global graph
    n = len(graph)
    table = [INF for i in range(n)]
    table[src] = 0
    queue = [[0, src]]

    while queue:
        cost, node = heapq.heappop(queue)
        if cost > table[node]: continue

        for nn, nc in graph[node]:
            distance = cost + nc
            if distance < table[nn]:
                table[nn] = distance
                heapq.heappush(queue, [distance, nn])

    return table[dst]


def solution(n, s, a, b, fares):
    Progress(n, fares)
    cost = dijkstra(s, a) + dijkstra(s, b)
    for i in range(1, n + 1):
        if s != i:
            cost = min(cost, dijkstra(s, i) + dijkstra(i, a) + dijkstra(i, b))
    return cost