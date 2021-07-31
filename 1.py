import sys
from collections import deque

sys.stdin = open("input.txt", "r")

T = str(input())
print(T, T[-1])
kyum = ""
index = 0
num = int(T[-1])
num2 = int(T[-2])
num3 = int(T[-3])
num2 = int(str(num2) + str(num))
num3 = int(str(num3) + str(num2) + str(num))
print(num2, 'zzz')
print(num3, 'zzz')
kyum += str(num)

while True:
    num -= 1
    kyum = str(num) + kyum
    if len(kyum) >= len(T):
        break

print(kyum, num)
