arr = ['A','E','I','O','U']
dic = []

def table(w):
    if len(w) == 6:
        return
    dic.append(w)
    for i in arr:
        table(w+i)

for i in arr:
    table(i)

print(dic)
print(dic.index('I') + 1)