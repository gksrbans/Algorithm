# -*- conding: utf-8 -*-

'''
Author : gksrbans123@gmail.com
Date : 2020-12-06
URL : https://programmers.co.kr/learn/courses/30/lessons/43164
Type : DFS / BFS
'''

# 출발지 간선으로 부터 도착지까지 그래프를 만든다.
# 해당 그래프의 값 들을 역순으로 정렬한다. -> 역순으로 정렬하는 이유는 알파벳 순서가 앞서는 경로를 먼저 pop
# 더이상 자식이 없거나 그래프에 없는 keys()들을 stack에서 빼서 visit배열에 append
# 추후 visit배열의 역순을 return 하여 답 출력.

def solution(tickets):
    graph = {}
    for key, value in tickets:
        # print(key,value)
        graph[key] = graph.get(key, []) + [value]
    # print(graph)

    for i in graph.keys():
        graph[i].sort(reverse=True)
    # print(graph)

    stack = ["ICN"]
    visit = []

    while stack:
        top = stack[-1]
        if top not in graph or len(graph[top]) == 0:
            visit.append(stack.pop())

        else:
            stack.append(graph[top][-1])
            graph[top].pop()

    return visit[::-1]






