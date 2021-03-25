import sys

sys.stdin = open("input.txt", "r")

N = int(input())
D = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    answer = 0
    for j in range(len(D[i])):
        if D[i][j] % 2 == 1:
            answer += D[i][j]

    print('#' + str(i+1) +" "+ str(answer))



