key, lock = [[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]


def rotated_90(arr):
    return list(zip(*arr[::-1]))


def attach(i, j, board, rotated_key, M):
    for x in range(M):
        for y in range(M):
            board[i + x][j + y] += rotated_key[i][j]


def detach(i, j, board, rotated_key, M):
    for x in range(M):
        for y in range(M):
            board[i + x][j + y] -= rotated_key[i][j]


def check(board, M, N):
    for i in range(N):
        for j in range(N):
            if board[M + i][M + j] != 1:
                return False;
    return True


def solution(key, lock):
    M, N = len(key), len(lock)

    board = [[0] * (M * 2 + N) for _ in range(M * 2 + N)]
    for i in range(N):
        for j in range(N):
            board[M + i][M + j] = lock[i][j]

    rotated_key = key
    for _ in range(4):
        rotated_key = rotated_90(rotated_key)
        for i in range(1, M + N):
            for j in range(1, M + N):
                # 열쇠 붙이기
                attach(i, j, board, rotated_key, M)

                # 가운데 check 하기
                if check(board, N, M):
                    return True
                # 열쇠 떼기
                detach(i, j, board, rotated_key, M)

    return False


print(key, lock)
