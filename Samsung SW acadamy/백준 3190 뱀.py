# -*- conding: utf-8 -*-

'''
Author : gksrbans123@gmail.com
Date : 2021-03-29
URL : https://www.acmicpc.net/problem/3190
Type : ?
'''

import sys
from collections import deque
import copy

sys.stdin = open("input.txt", "r")

N = int(input())
board = [[0] * N for _ in range(N)]
K = int(input())

for i in range(K):
    mac_n, mac_m = input().split()
    #print(mac_n, mac_m)
    board[int(mac_n) - 1][int(mac_m) - 1] = "MAC"  # 사과가 있을 경우 1

L = int(input())
times = {}
for i in range(L):
    X, C = input().split()
    times[int(X)] = C
#print(times)
#print(board)

# 뱀은 몸길이를 늘려서 머리를 다음칸에 위치함.
# 먄약 이동한 칸에 사과가 있다면 그칸에 사과가 없어지고 꼬리는 움직이지 않음.
# 이동한 칸에 사과가 없다면 꼬리가 위치한 칸을 비워준다. => 몸길이 안변함

def change(dir, C):
    # 상 우 하 좌 (0 ,1, 2, 3)
    # 좌 상 우 하 // 왼쪽 (3, 0, 1, 2)
    if C == 'L':
        dir = (dir-1) % 4

    # 우 하 좌 상 // 오른쪽 (1, 2, 3, 0)
    else:
        dir = (dir+1) % 4

    return dir


row, column = 0, 0
q = deque([[row, column]])
direction = 1
time = 1
# 상 우 하 좌
dy = [-1, 0, 1, 0]  # row dy
dx = [0, 1, 0, -1]  # col dx
board[row][column] = 2

flag = True
while flag:
    row, column = row + dy[direction], column + dx[direction]
    if 0 <= row < N and 0 <= column < N and board[row][column] != 2:  # 판 때기 안에있을 때
        if board[row][column] != "MAC": # 사과가 없을 때
            temp_x, temp_y = q.popleft()
            board[temp_x][temp_y] = 0  # 꼬리 제거하기

        # 사과 있으면 꼬리를 제거하지만 않으면 됨.
        board[row][column] = 2
        q.append([row, column])

        if time in times.keys():
            direction = change(direction, times[time])
        time += 1

    else:
        print(time)
        flag = False

