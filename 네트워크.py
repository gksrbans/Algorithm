# -*- conding: utf-8 -*-

'''
Author : gksrbans123@gmail.com
Date : 2020-12-02
URL : https://programmers.co.kr/learn/courses/30/lessons/43162
Type : DFS / BFS
'''



# n을 기준으로 탐색.
# 방문했던 노드는 visit 리스트에 True 로 바꿔줌
# DFS 탐색하면서, 컴터번호를 넣고 연결된 자식노드를 다시 배열에 넣어줌
# 배열에 넣을게 없을 경우 (empty) 최종 노드이므로 answer를 +1 증가시켜 주고 dfs를 빠져나옴


def dfs(computers, visited, start):
    record = [start]
    while record:
        temp = record.pop()
        if visited[temp] == 0:
            visited[temp] = 1
        for i in range(0, len(computers)):
            if computers[temp][i] == 1 and visited[i] == 0: # 2차원 배열의 내 각각의 원소들로부터 그 원소가 만약 이어져있으면서, 방문하지 않았던 노드면 레코드에 추가해줌.
                record.append(i)


def solution(n, computers):
    answer = 0
    visited = [0 for _ in range(n)]
    start = 0

    while 0 in visited:
        if visited[start] == 0: # 방문하지 않은 노드일 경우.
            dfs(computers, visited, start) # dfs 실행!
            answer += 1 # 네트워크가 없는 상태니까 +1 해줌.

        start += 1
    return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))

