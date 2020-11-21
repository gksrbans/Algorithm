# -*- conding: utf-8 -*-

'''
Author : gksrbans123@gmail.com
Date : 2020-11-21
URL : https://programmers.co.kr/learn/courses/30/lessons/43105
Type : Dynamic Programming
'''

def solution(triangle):
    for i in range(1, len(triangle)):
        for j in range(i+1):
            if j == 0:
                triangle[i][j] += triangle[i-1][j]
            elif j == i:
                triangle[i][j] += triangle[i-1][j-1]
            else:
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
    return max(triangle[-1])

######################################################################
# 처음에 DFS 완전 탐색을 통해서 모든 노드의 합이 될수있는 경우를 찾아 max값을 출력할려고 했었으나
# 아주 잘못된 생각이였음을 느꼈다.
# 이진트리의 양 싸이드는 바로 위에 숫자를 더해서 그대로 가져오고 가운데 값의 경우에 왼쪽,오른쪽중에 큰것을 더해서 트리를 완성시킨다.

# | refer : https://codedrive.tistory.com/49

# def dfs(graph, start_node):
#     visited = list()
#     stack = list()
#
#     stack.append(start_node)
#
#     while stack:
#         node = stack.pop()
#         print(node, 'node임')
#         if node not in visited:
#             visited.append(node)
#             stack.extend(reversed(graph[node]))
#             print(stack, '스택임')
#
#     return visited