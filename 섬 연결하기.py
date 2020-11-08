# -*- conding: utf-8 -*-

'''
Author : gksrbans123@gmail.com
Date : 2020-11-08
URL : https://programmers.co.kr/learn/courses/30/lessons/42861
Type : Greedy
'''

# 코딩 전에 Union_find 알고리즘 및 크루즈칼 알고리즘 숙지!

parent={}
rank={}

def make_set(node):
    parent[node] = node
    rank[node] = 0

def find(node):
    if parent[node] != node:
        #print('err')
        parent[node] = find(parent[node])
    return parent[node]

def union(node_v, node_u):
    root1 = find(node_v)
    root2 = find(node_u)

    if rank[root1] > rank[root2]:
        parent[root2] = root1

    else:
        parent[root1] = root2
        if rank[root1] == rank[root2]:
            rank[root2] += 1


def solution(n, costs):

    mst = list()

    mygraph = {
        'vertices': [],
        'edges':[]
    }

    for i in range(n):
        mygraph['vertices'].append(str(i))

    for i in range(len(costs)):
        mygraph['edges'].append((costs[i][2], str(costs[i][0]), str(costs[i][1])))

    # print(mygraph)
    for node in mygraph['vertices']:
        # print(node, 'node임')
        make_set(node)

    edges = mygraph['edges']
    edges.sort()

    for edge in edges:
        weight, node_v, node_u = edge
        # print(find(node_v), find(node_u))
        if find(node_v) != find(node_u):
            union(node_v, node_u)
            mst.append(edge)

    answer = 0
    for i in mst:
        answer += i[0]

    return answer

####################################################################





