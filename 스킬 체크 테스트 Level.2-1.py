# -*- conding: utf-8 -*-

'''
Author : gksrbans123@gmail.com
Date : 2020-09-22
URL : https://programmers.co.kr/skill_checks/183692
Info : fail...
'''


N = 8
A = 1
B = 8

sum = -1
answer = 0

while N:
    N = N // 2
    sum += 1

for i in range(sum):
    A = A // 2
    B = B // 2
    #print(B)
    if A != 1 and A % 2 != 0:
        A = A + 1
    if B != 1 and B % 2 != 0:
        B = B + 1
    print(A, B, i)

    if B - A == 1:
        answer = i + 2
        break
    else:
        pass

print(answer)