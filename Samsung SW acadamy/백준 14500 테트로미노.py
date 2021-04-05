# -*- conding: utf-8 -*-

'''
Author : gksrbans123@gmail.com
Date : 2021-04-04
URL : https://www.acmicpc.net/problem/14500
Type : ?
'''

import sys

sys.stdin = open("input.txt", "r")
# N, M = map(int, input().split())
# board = [list(map(int, input().split())) for _ in range(N)]
# result = []
#
#
# def long_stick():
#     answer = []
#     for i in range(N):
#         for j in range(M - 3):
#
#             plus = 0
#             for k in range(4):
#                 # print(board[i][j + k])
#                 plus += board[i][j + k]
#             # print(plus, 'd')
#             answer.append(plus)
#     return max(answer)
#
#
# def long_stick_90():
#     answer = []
#     for i in range(N - 3):
#         for j in range(M):
#             plus = 0
#             for k in range(4):
#                 plus += board[i + k][j]
#             answer.append(plus)
#     return max(answer)
#
#
# def square():
#     answer = []
#     for i in range(N - 1):
#         for j in range(M - 1):
#             plus = 0
#             for n in range(2):
#                 for m in range(2):
#                     plus += board[i + n][j + m]
#             answer.append(plus)
#             # print(answer, '1')
#     return max(answer)
#
#
# def L():
#     answer = []
#     for i in range(N - 2):
#         for j in range(M - 1):
#             plus = 0
#             plus += board[i][j] + board[i + 1][j] + board[i + 2][j] + board[i + 2][j + 1]
#             answer.append(plus)
#     return max(answer)
#
#
# def L_90():
#     answer = []
#     for i in range(N - 1):
#         for j in range(M - 2):
#             plus = 0
#             plus += board[i][j] + board[i][j + 1] + board[i][j + 2] + board[i + 1][j]
#             answer.append(plus)
#     return max(answer)
#
#
# def L_180():
#     answer = []
#     for i in range(N - 2):
#         for j in range(M - 1):
#             plus = 0
#             plus += board[i][j] + board[i][j + 1] + board[i + 1][j + 1] + board[i + 2][j + 1]
#             answer.append(plus)
#     return max(answer)
#
#
# def L_270():
#     answer = []
#     for i in range(N - 1):
#         for j in range(2, M - 2):
#             plus = 0
#             plus += board[i][j] + board[i][j + 1] + board[i][j + 2] + board[i - 1][j + 2]
#             answer.append(plus)
#     return max(answer)
#
#
# def S_L():
#     answer = []
#     for i in range(2, N):
#         for j in range(M-1):
#             plus = 0
#             plus += board[i][j] + board[i][j+1] + board[i-1][j+1] + board[i-2][j+1]
#             answer.append(plus)
#     return max(answer)
#
#
# def S_L_90():
#     answer = []
#     for i in range(N-1):
#         for j in range(M-2):
#             plus = 0
#             plus += board[i][j] + board[i+1][j] + board[i+1][j + 1] + board[i+1][j + 2]
#             answer.append(plus)
#     return max(answer)
#
#
# def S_L_180():
#     answer = []
#     for i in range(N-2):
#         for j in range(M-1):
#             plus = 0
#             plus += board[i][j] + board[i][j+1] + board[i+1][j + 1] + board[i+2][j + 1]
#             answer.append(plus)
#     return max(answer)
#
#
# def S_L_270():
#     answer = []
#     for i in range(1, N):
#         for j in range(M-2):
#             plus = 0
#             plus += board[i][j] + board[i][j+1] + board[i][j + 2] + board[i-1][j + 2]
#             answer.append(plus)
#     return max(answer)
#
# def Z():
#     answer = []
#     for i in range(1, N):
#         for j in range(M - 2):
#             plus = 0
#             plus += board[i][j] + board[i][j + 1] + board[i - 1][j + 1] + board[i - 1][j + 2]
#             answer.append(plus)
#     return max(answer)
#
#
# def Z_90():
#     answer = []
#     for i in range(N - 2):
#         for j in range(M - 1):
#             plus = 0
#             plus += board[i][j] + board[i + 1][j] + board[i + 1][j + 1] + board[i + 2][j + 1]
#             answer.append(plus)
#     return max(answer)
#
# def S_Z():
#     answer = []
#     for i in range(N-1):
#         for j in range(M - 2):
#             plus = 0
#             plus += board[i][j] + board[i][j + 1] + board[i + 1][j + 1] + board[i + 1][j + 2]
#             answer.append(plus)
#     return max(answer)
#
#
# def S_Z_90():
#     answer = []
#     for i in range(2, N):
#         for j in range(M - 1):
#             plus = 0
#             plus += board[i][j] + board[i-1][j] + board[i-1][j + 1] + board[i-2][j + 1]
#             answer.append(plus)
#     return max(answer)
#
#
# def T():
#     answer = []
#     for i in range(N - 1):
#         for j in range(M - 2):
#             plus = 0
#             plus += board[i][j] + board[i][j + 1] + board[i + 1][j + 1] + board[i][j + 2]
#             answer.append(plus)
#     return max(answer)
#
#
# def T_90():
#     answer = []
#     for i in range(N - 2):
#         for j in range(1, M):
#             plus = 0
#             plus += board[i][j] + board[i + 1][j] + board[i + 1][j - 1] + board[i + 2][j]
#             answer.append(plus)
#     return max(answer)
#
#
# def T_180():
#     answer = []
#     for i in range(1, N):
#         for j in range(M - 2):
#             plus = 0
#             plus += board[i][j] + board[i][j + 1] + board[i - 1][j + 1] + board[i][j + 2]
#             answer.append(plus)
#     return max(answer)
#
#
# def T_270():
#     answer = []
#     for i in range(N - 2):
#         for j in range(M - 1):
#             plus = 0
#             plus += board[i][j] + board[i + 1][j] + board[i + 1][j + 1] + board[i + 2][j]
#             answer.append(plus)
#     return max(answer)
#
#
# result.append(long_stick())
# result.append(long_stick_90())
# result.append(square())
# result.append(L())
# result.append(L_90())
# result.append(L_180())
# result.append(L_270())
# result.append(Z())
# result.append(Z_90())
# result.append(T())
# result.append(T_90())
# result.append(T_180())
# result.append(T_270())
#
# result.append(S_L())
# result.append(S_L_90())
# result.append(S_L_180())
# result.append(S_L_270())
#
# result.append(S_Z())
# result.append(S_Z_90())
#
# print(result)
# print(max(result))

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
tetromino = [
    [(0, 0), (0, 1), (1, 0), (1, 1)],  # ㅁ
    [(0, 0), (0, 1), (0, 2), (0, 3)],  # ㅡ
    [(0, 0), (1, 0), (2, 0), (3, 0)],  # ㅣ
    [(0, 0), (0, 1), (0, 2), (1, 0)],
    [(1, 0), (1, 1), (1, 2), (0, 2)],
    [(0, 0), (1, 0), (1, 1), (1, 2)],  # ㄴ
    [(0, 0), (0, 1), (0, 2), (1, 2)],  # ㄱ
    [(0, 0), (1, 0), (2, 0), (2, 1)],
    [(2, 0), (2, 1), (1, 1), (0, 1)],
    [(0, 0), (0, 1), (1, 0), (2, 0)],
    [(0, 0), (0, 1), (1, 1), (2, 1)],
    [(0, 0), (0, 1), (0, 2), (1, 1)],  # ㅜ
    [(1, 0), (1, 1), (1, 2), (0, 1)],  # ㅗ
    [(0, 0), (1, 0), (2, 0), (1, 1)],  # ㅏ
    [(1, 0), (0, 1), (1, 1), (2, 1)],  # ㅓ
    [(1, 0), (2, 0), (0, 1), (1, 1)],
    [(0, 0), (1, 0), (1, 1), (2, 1)],
    [(1, 0), (0, 1), (1, 1), (0, 2)],
    [(0, 0), (0, 1), (1, 1), (1, 2)]
]


def find(x, y):
    global answer
    for i in range(19):
        result = 0
        for j in range(4):
            try:
                next_x = x + tetromino[i][j][0]  # x 좌표
                next_y = y + tetromino[i][j][1]  # y 좌표
                result += board[next_x][next_y]
            except IndexError:
                continue
        answer = max(answer, result)


def solve():
    for i in range(n):
        for j in range(m):
            find(i, j)


answer = 0
solve()
print(answer)

