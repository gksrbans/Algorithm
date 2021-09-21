from collections import deque

enter, leave = [1, 4, 2, 3], [2, 1, 4, 3]

answer = [0 for _ in range(len(enter)+1)]
leave = deque(leave)

room = []
for i in enter:
    print(i, '등장')
    print(answer, room, '등장 후 answer')
    for r in room:
        answer[r] += 1 # 입실했는데 방안에 사람이 있으면 만남.
        print(r, '만낫당')
    answer[i] += len(room)

    room.append(i) # 방에 입실

    print(room, '떠나기전 방상태')
    while leave and leave[0] in room:
        print(leave, 'leave 로깅')
        room.remove(leave.popleft())

print(answer)





    