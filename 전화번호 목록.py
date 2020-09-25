# -*- conding: utf-8 -*-

'''
Author : gksrbans123@gmail.com
Date : 2020-09-25
URL : https://programmers.co.kr/learn/courses/30/lessons/42577
Type : Hash
'''

def wjqentk(list1, list2):
    length = len(list1)
    if list1 == list2[:length]:
        return False
    else:
        return True

def solution(phone_book):
    answer = True
    phone_book.sort()
    # sort를 꼭 해줘야함!
    for i in range(len(phone_book)-1):
        for j in range(i+1, len(phone_book)):
            #print(i, j, phone_book[i], phone_book[j])
            if wjqentk(phone_book[i], phone_book[j]) == False:
                return False
            else:
                pass               
    return answer

########################################################

# 첫 번째 작성 코드..
# 중간에 문자가 들어가 있을 경우에 테스트케이스를 통과 불가능. EX_ '945' 과 '1239459402'
# 945가 중간에 들어가 있어서 안됌.

# def solution(phone_book):
#     answer = True
#     for i in range(len(phone_book) - 1):
#         for j in range(i + 1, len(phone_book)):
#             # print(i, j, phone_book[i], phone_book[j])
#             if phone_book[i] in phone_book[j]:
#                 # print(i, j, phone_book[i], phone_book[j])
#                 answer = False
#
#     return answer
########################################################

# 다른 사람의 풀이에 startswith 메서드 보면서 현타
# 근데 이렇게 짜면 앞뒤 꺼만 zip으로 묶여서 모든 경우의 수를 확인하지 못하는데 왜 통과하는지는 모르겠다.
# O(N^N)

# def solution(phoneBook):
#     phoneBook = sorted(phoneBook)
#
#     for p1, p2 in zip(phoneBook, phoneBook[1:]):
#         if p2.startswith(p1):
#             return False
#     return True

########################################################