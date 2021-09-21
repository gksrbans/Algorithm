weights, head2head = [60, 70, 60], ["NNN", "NNN", "NNN"]
L = len(weights)

arr = []
answer = []

print(L, '길이')

for i in range(len(head2head)):
    temp = []
    print(i, 'ㅎㅎ')
    temp.append(head2head[i].count('W') / (head2head[i].count('W') + head2head[i].count('L')) * 100) # 승률
    
    tmp = 0
    for j in range(len(head2head[i])):
        #print(weights[i] , weights[j], '몸무게비교')
        if head2head[i][j] == 'W' and weights[i] < weights[j]:
            tmp += 1
    
    temp.append(tmp)
    temp.append(weights[i])
    temp.append(-i)

    arr.append(temp)

print(arr)
arr = sorted(arr, reverse=True)
print(arr)
for i in arr:
    answer.append(i[4]+ 1)

print(answer)
