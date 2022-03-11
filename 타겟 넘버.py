from collections import deque

numbers, target = [4, 1, 2, 1], 4

answer = 0
queue = deque()
n = len(numbers)

print(n)
queue.append([numbers[0], 0])
queue.append([-numbers[0], 0])
print(queue, '첫번째 큐')
while queue:
    temp, idx = queue.popleft()
    print(temp, idx, '팝팝', queue)
    idx += 1
    if idx < n:
        queue.append([temp+numbers[idx], idx])
        queue.append([temp-numbers[idx], idx])
    else:
        if temp == target:
            answer += 1


print(answer, '답임')