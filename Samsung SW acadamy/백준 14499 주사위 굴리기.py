# -*- conding: utf-8 -*-

'''
Author : gksrbans123@gmail.com
Date : 2021-04-04
URL : https://www.acmicpc.net/problem/14499
Type : ?
'''

import sys

sys.stdin = open("input.txt", "r")

N, M, x, y, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
commands = list(map(int, input().split()))
direct = {1: (0, 1), 2: (0, -1), 3: (-1, 0), 4: (1, 0)}  # 마지막 줄에는 이동하는 명령이 순서대로 주어진다. 동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4로 주어진다.
dice = [0] * 7
#print(dice)

for command in commands:
    dx, dy = direct[command]
    x += dx
    y += dy
    if 0 <= x < N and 0 <= y < M:
        if command == 1:  # 동쪽 1,3,4,6
            dice[3], dice[1] = dice[1], dice[3]
            dice[1], dice[4] = dice[4], dice[1]
            dice[4], dice[6] = dice[6], dice[4]

        elif command == 2:  # 서쪽 1,3,4,6
            dice[4], dice[1] = dice[1], dice[4]
            dice[1], dice[3] = dice[3], dice[1]
            dice[3], dice[6] = dice[6], dice[3]

        elif command == 3:  # 북쪽 2,1,5,6
            dice[2], dice[1] = dice[1], dice[2]
            dice[1], dice[5] = dice[5], dice[1]
            dice[5], dice[6] = dice[6], dice[5]

        elif command == 4:  # 남쪽 2,1,5,6
            dice[5], dice[1] = dice[1], dice[5]
            dice[1], dice[2] = dice[2], dice[1]
            dice[2], dice[6] = dice[6], dice[2]

        if board[x][y]==0: # 칸이 0 이면 -> 주사위에 있는값이 복사됨
            board[x][y]=dice[6]
        else:   # 주사위 값 교체
            dice[6]=board[x][y]
            board[x][y]=0
        print(dice[1])

    else:
        x -= dx
        y -= dy