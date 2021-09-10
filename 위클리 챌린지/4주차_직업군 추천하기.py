from collections import deque
table, languages, preference =	["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"], ["JAVA", "JAVASCRIPT"], [7, 5]

new_list = list(zip(languages, preference))
ret = 0

q = deque()
q.append('tmp')

for i in table:
    i = i.split(' ')
    print(i)
    #print(6 - i.index(j[0])
    tmp = 0
    for j in new_list:
        try:
            tmp += j[1] * (6 - i.index(j[0]))
        except:
            tmp += 0

    print(tmp, 'tt')

    if tmp > ret:
        q.append(i[0])
        q.popleft()
        ret = max(tmp, ret)

    elif tmp == ret:
        q.append(i[0])
    

q = sorted(q)
print(q)
