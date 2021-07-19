import sys

sys.stdin = open('input.txt', 'r')
N, M = map(int, input().split(' '))
files = []

for _ in range(N):
    name, ext = input().split('.')
    files.append([name, 0, ext])

#print(files)
dic = {}
for i in range(M):
    temp = input()
    dic[temp] = ''

#print(dic)

for i in range(N):
    if files[i][2] not in dic:
        files[i][1] = 1
#print(files)
files = sorted(files)
#print(files)

for i in range(N):
    print(f'{files[i][0]}.{files[i][2]}')