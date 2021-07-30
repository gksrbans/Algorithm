from itertools import combinations

relation =	[["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"], ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]
relation.sort()
row = len(relation)
col = len(relation[0])

arr = []
for i in range(1, col+1):
    arr.extend(combinations(range(col), i))

#print(arr)

unique = []
for candi in arr:
    temp = [tuple([item[i] for i in candi]) for item in relation]
    #print(temp)
    #print(set(temp), 'setsetset')
    if len(set(temp)) == row:
        unique.append(candi)
#print(unique)
#print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
# for item in arr:
#     temp2 = []
#     print(item)
#     for j in relation:
#         #print(j)
#         tmp3 = []
#         for v in item:
#             tmp3.append(j[v])
#         temp2.append(tmp3)
#     print(temp2)

answer = set(unique)
for i in range(len(unique)):
    for j in range(i+1, len(unique)):
        #print(unique[i], unique[j])
        if len(unique[i]) == len(set(unique[i]).intersection(set(unique[j]))):
            answer.discard(unique[j])

print(answer)