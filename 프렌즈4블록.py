def solution(m, n, board):
    for _ in range(len(board)):
        temp = board.pop(0)
        board.append(list(temp))
    answer = 0
    while True:
        temp = []
        #print(board)
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] == "0":
                    continue

                if board[i+1][j] == board[i][j+1] == board[i+1][j+1] == board[i][j]:
                    #print('야호', i, j)
                    temp.append((i, j))
                    temp.append((i+1, j))
                    temp.append((i, j+1))
                    temp.append((i+1, j+1))

        temp = list(set(temp))
        #print(temp)

        if len(temp) == 0:
            break
        else:
            answer += len(temp)
            for row, col in temp:
                board[row][col] = '0'

            for row, col in temp:
                #print(row, col, 'dd?', board[row][col], board[row-1][col])
                new_row = row-1 # 한칸 위의 row

                while new_row >= 0:
                    if board[row][col] == '0' and board[new_row][col] != '0': # 터진 블록인데 위에 내려올게 있을 경우
                        #print(row, col, 'this')
                        board[row][col] = board[new_row][col] # 블록 내리기
                        board[new_row][col] = '0' # 내려진 블록 있던자리 빈칸으로

                        row -= 1 # 다음 단계 row로

                    new_row -= 1

    #print(board)
    return answer