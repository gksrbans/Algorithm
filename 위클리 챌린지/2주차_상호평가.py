scores = 	[[70, 49, 90], [68, 50, 38], [73, 31, 100]]

new_list = list(map(list, zip(*scores)))
answer = ""
print(new_list)

for i, v in enumerate(new_list):
    _max = max(v)
    _min = min(v)
    print(i,v, _max, _min)

    if v.count(v[i]) < 2 and (v[i] == _max or v[i] == _min):
        v.pop(i)
    print(v, '바뀜')

    tmp = sum(v) / len(v)
    if tmp >= 90:
        answer += "A"
    elif 80<=tmp<90:
        answer += "B"
    elif 70<=tmp<80:
        answer += "C"
    elif 50<=tmp<70:
        answer += "D"
    else:
        answer += "F"

print(answer)


    