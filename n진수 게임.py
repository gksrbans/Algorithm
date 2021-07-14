def change_num(num, q):
    base = ''

    while num > 0:
        num, mod = divmod(num, q)
        if mod == 10:
            mod = 'A'
        elif mod == 11:
            mod = 'B'
        elif mod == 12:
            mod = 'C'
        elif mod == 13:
            mod = 'D'
        elif mod == 14:
            mod = 'E'
        elif mod == 15:
            mod = 'F'
        base += str(mod)
    return base[::-1]


def solution(n, t, m, p):
    arr = ['0']
    answer = []
    for i in range(t * m):
        arr.extend(list(change_num(i, n)))

    for i in range(t):
        answer.append(arr[p - 1])
        p = p + m

    return ''.join(answer)