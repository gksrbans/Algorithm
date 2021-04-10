# -*- conding: utf-8 -*-

'''
Author : gksrbans123@gmail.com
Date : 2021-04-05
URL : https://www.acmicpc.net/problem/14503
Type : ?
'''

import sys

sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
r, c, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
count = 0
#print(board)

# 북 0, 동 1, 남 2, 서 3
# 서, 북, 동, 남  => 현재기준방향 왼쪽 시 d+3 % 4
# 남, 서, 북, 동 => 뒤로 d+2 % 4
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def clean(r, c, d):
    global count
    if board[r][c] == 0:
        board[r][c] = 2
        count += 1

    for _ in range(4):
        # 새로운 방향과 좌표 정의
        nd = (d + 3) % 4
        nr = r + dx[nd]
        nc = c + dy[nd]

        if board[nr][nc] == 0:
            clean(nr, nc, nd)
            return
        d = nd

    # 뒤로가기 구현
    nd = (d + 2) % 4
    nr = r + dx[nd]
    nc = c + dy[nd]
    if board[nr][nc] == 1:
        return
    clean(nr, nc, d)

clean(r, c, d)
print(count)