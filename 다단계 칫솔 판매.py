from collections import deque

enroll, referral, seller, amount = 	["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], ["young", "john", "tod", "emily", "mary"], [12, 4, 2, 5, 10]
zigap_hash = {}
for i in enroll:
    zigap_hash[i] = 0

for i in range(len(amount)):
    amount[i] = amount[i] * 100
x = list(zip(enroll, referral))
insert = list(zip(seller, amount))
print(insert)



def bfs(name, done):
    remain_price = 0 if int(done * 0.1) < 1 else int(done * 0.1) # 0.1
    self_price = done - remain_price #0.9

    zigap_hash[name] += self_price

    discover = []
    q = deque([name])

    while q:
        print(q, 'qq')
        v = q.pop()
        for w in x:
            if w[0] == v and w[1] != "-":
                print(w, '들어오긴함 ?')
                if w[1] not in discover:
                    #print(w[1], remain_price, 'mary찾는중')
                    temp = 0 if int(remain_price * 0.1) < 1 else int(remain_price * 0.1)
                    #print(temp, remain_price)
                    remain_price = remain_price - temp
                    zigap_hash[w[1]] += remain_price
                    remain_price = temp

                    discover.append(w[1])
                    q.append(w[1])

    return
answer = []
for i in insert:
    bfs(i[0], i[1])
for i in zigap_hash.values():
    answer.append(int(i))

print(answer)
# print(bfs('young',1200))
# print(zigap_hash, 'ddd')