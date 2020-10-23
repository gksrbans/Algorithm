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


##################################################################

# 다른 사람이 풀이...
# 이렇게 깔끔하게 짤수가 있구나!

# numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
# hand = "left"

# number_dict = {1:(0,0),2:(1,0),3:(2,0),
#                4:(0,1),5:(1,1),6:(2,1),
#                7:(0,2),8:(1,2),9:(2,2),
#                '*':(0,3),0:(1,3),'#':(2,3),}

# left_hand = [1,4,7]
# right_hand = [3,6,9]
# l_hand = '*'
# r_hand = '#'
# answer = ''

# for i in numbers:
#     if i in left_hand:
#         answer += 'L'
#         l_hand = i
#     elif i in right_hand:
#         answer += 'R'
#         r_hand = i
#     else:
#         temp = number_dict[i]
#         lPos = number_dict[l_hand]
#         rPos = number_dict[r_hand]

#         l_range = abs(temp[0] - lPos[0]) + abs(temp[1] - lPos[1])
#         r_range = abs(temp[0] - rPos[0]) + abs(temp[1] - rPos[1])

#         if l_range < r_range:
#             answer += 'L'
#             l_hand = i
#         elif l_range > r_range:
#             answer += 'R'
#             r_hand = i
#         else:
#             if hand == 'left':
#                 answer += 'L'
#                 l_hand = i
#             else:
#                 answer += 'R'
#                 r_hand = i
# print(answer)

##################################################################
