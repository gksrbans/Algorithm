import sys
from collections import deque

sys.stdin = open('input.txt', 'r')
q = deque()

N,T,W = map(int, input().split(' '))
for _ in range(N):
    index, wait_time = map(int, input().split(' '))
    q.append([index, wait_time, 0])

#print(q)

M = int(input())
dic = {}
for i in range(M):
    index, wait_time, come_time = map(int, input().split(' '))
    dic[come_time] = [index, wait_time, 0]

#print(dic)

for i in range(W):
    if i in dic:
        q.append(dic[i]) # 대기손님 입장
    if q[0][1] == 0:
        q.popleft() # 맨 앞 손님의 대기시간이 0이면 퇴장

    elif q[0][2] == T:
        q[0][2] == 0 # 맨 앞 손님이 T초만큼 지났는데도 일이 남아있으면 0으로만들고 큐의 왼쪽에서 제거해서 마지막에 다시 넣어줌
        temp = q.popleft()
        q.append(temp)

    else:
        pass

    # The time goes on
    q[0][1] -= 1 # 맨 앞사람 1초씩 소요
    q[0][2] += 1 # 맨 앞사람이 소요된 시간을 저장.

    print(f'{q[0][0]}')
