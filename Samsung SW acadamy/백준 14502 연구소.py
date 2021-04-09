# -*- conding: utf-8 -*-

'''
Author : gksrbans123@gmail.com
Date : 2021-04-05
URL : https://www.acmicpc.net/problem/14502
Type : ?
'''

import sys
import copy


sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

# 상 하 좌 우
dx = [-1,1,0,0]
dy = [0,0,-1,1]
clean_zone = 0

# 벽 3개 선택하기
def wall(start, count):
    global clean_zone
    if count == 3:
        temp_board = copy.deepcopy(board)
        for row in range(N):
            for col in range(M):
                virus(temp_board, row, col)
        clean = sum(i.count(0) for i in temp_board)
        clean_zone = max(clean_zone, clean)
        return

    else:
        for i in range(start, N*M):
            r = i // M # row는 전체 갯수를 col갯수로 나눈 몫
            c = i % M # col은  전체 갯수를 col 개수로 나눈 나머지.
            if board[r][c] == 0:
                board[r][c] = 1
                wall(i, count+1)
                board[r][c] = 0

# 바이러스 퍼뜨리기
def virus(board, row, col):
    if board[row][col] == 2:
        for i in range(4):
            n_row = row + dx[i]
            n_col = col + dy[i]
            if 0 <= n_row < N and 0 <= n_col < M: # 보드안에서
                if board[n_row][n_col] == 0:
                    board[n_row][n_col] = 2
                    virus(board, n_row, n_col)

wall(0,0)
print(clean_zone)