# -*- conding: utf-8 -*-

'''
Author : gksrbans123@gmail.com
Date : 2021-04-25
URL : https://www.acmicpc.net/problem/2667
Type : DFS
'''
import sys

sys.stdin = open("input.txt", "r")
N = int(input())

board = [list(map(int, input())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
cnt = 1 # 집 단지별 번호
nums = 0 # 단지 갯수를 세기위한 변수
result = [] # num 합계를 result에 반환

# 상 하 좌 우 변수
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def DFS(row, col, cnt):
    global nums

    visited[row][col] = 1 # 방문으로 바꿔줌
    if board[row][col] == 1:
        board[row][col] = cnt # 집 단지 반영
        nums += 1 # 집갯수 증


    for i in range(4):
        ny = row + dy[i]
        nx = col + dx[i]

        if 0 <= ny < N and 0<= nx < N: #보드 안에 있다면,
            if board[ny][nx] == 1 and visited[ny][nx] == 0: # 새로운 좌표에 집이 있고 방문하지 않았다면, DFS
                DFS(ny, nx, cnt)

for i in range(N):
    for j in range(N):
        if board[i][j] == 1 and visited[i][j] == 0: # 집이 있으면서 방문한적이 없다면 DFS
            DFS(i, j, cnt)
            result.append(nums)
            nums = 0
            cnt += 1

print(len(result))
for i in sorted(result):
    print(i)
