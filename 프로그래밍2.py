dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def solution(places):
    answer = []
    for place in places:
        board = []
        flag = 1

        for i in place:
            temp = []
            for j in i:
                temp.append(j)
            board.append(temp)
        for row in range(5):
            for col in range(5):
                if board[row][col] == 'P':
                    for i in range(4):
                        # 인접
                        ny = row + dy[i]
                        nx = col + dx[i]

                        if 0 <= ny < 5 and 0 <= nx < 5:
                            if board[ny][nx] == 'P':
                                flag = 0
                            if board[ny][nx] == 'O':
                                for i in range(4):
                                    xy = ny + dy[i]
                                    xx = nx + dx[i]
                                    temp = abs(row - xy) + abs(col - xx)
                                    # print(temp)
                                    if 0 <= xy < 5 and 0 <= xx < 5:
                                        if (xy != row and xx != col) and board[xy][xx] == 'P' and temp <= 2: flag = 0

        answer.append(flag)
    return answer