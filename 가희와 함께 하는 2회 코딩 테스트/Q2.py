import sys

sys.stdin = open('input.txt', 'r')

N,M = map(int, input().split(' '))
note = {}

for _ in range(N):
    note[input()] = '1'

for _ in range(M):
    temp = input().split(',')
    for j in temp:
        if j in note:
            note.pop(j)

    print(len(note))

    
