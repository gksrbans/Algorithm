# -*- conding: utf-8 -*-

'''
Author : gksrbans123@gmail.com
Date : 2020-10-21
URL : https://programmers.co.kr/learn/courses/30/lessons/67256
Type : 카카오 가즈아
'''

def L_range(start,find):
    matrix = [[1,4,7,'*'], [2,5,8,0], [3,6,9,'#']]
    matrix2 = [[1,2,3], [4,5,6], [7,8,9], ['*', 0, '#']]

    temp = 0
    for i in range(len(matrix)):

        if start in matrix[i]:
            temp += i
        if find in matrix[i]:
            temp -= i


    temp2 = 0
    for i in range(len(matrix2)):
        if start in matrix2[i]:
            temp2 += i
        if find in matrix2[i]:
            temp2 -= i


    return abs(temp) + abs(temp2)


def R_range(start, find):
    matrix = [[3,6,9,'#'],[2,5,8,0],[1,4,7,'*']]
    matrix2 = [[1,2,3], [4,5,6], [7,8,9], ['*', 0, '#']]

    temp = 0
    for i in range(len(matrix)):

        if start in matrix[i]:
            temp += i
        if find in matrix[i]:
            temp -= i

    temp2 = 0
    for i in range(len(matrix2)):

        if start in matrix2[i]:
            temp2 += i
        if find in matrix2[i]:
            temp2 -= i


    return abs(temp) + abs(temp2)


def solution(numbers, hand):
    answer = ''
    L_start = '*'
    R_start = '#'

    for i in range(len(numbers)):
#        print(numbers[i])
        if numbers[i] == 1 or numbers[i] == 4 or  numbers[i] == 7 or  numbers[i] == '*':
            answer += 'L'
            L_start = numbers[i]
        elif numbers[i] == 3 or numbers[i] == 6 or numbers[i] == 9 or numbers[i] == '#':
            answer += 'R'
            R_start = numbers[i]
        else:
            try:
                find = numbers[i]
                L = L_range(L_start, find)
                R = R_range(R_start, find)

                if L < R:
                    answer +='L'
                    L_start = numbers[i]
                elif L > R:
                    answer +='R'
                    R_start = numbers[i]
                else:

                    if hand == 'right':
                        answer += 'R'
                        R_start = numbers[i]
                    else:
                        answer += 'L'
                        L_start = numbers[i]
            except:
                pass

    return answer