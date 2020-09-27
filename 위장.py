# -*- conding: utf-8 -*-

'''
Author : gksrbans123@gmail.com
Date : 2020-09-27
URL : https://programmers.co.kr/learn/courses/30/lessons/42578
Type : Hash
'''


import collections
import itertools

def solution(clothes):
    result = []
    answer = 1
    
    for i  in range(len(clothes)):
        result.append(clothes[i][1])
        
    result = collections.Counter(result)
        
    for i in result.values():
        answer *= (i + 1)
        # 의상을 안입었을 경우의 수 1을 더할 것임.
        
    return answer - 1
    # 아무것도 입지않은 스파이 -1



################################################

# 첫번 째 실패코드.
# ㅡ> 모두다 입었다는 가정하에 조합을 했고, 거기에 개별 의상의 갯수만 플러스함.
# return 할 때 키값이 1인거만 제외하고 return을 받았었음
# 문제는 {6,1,1} 인 경우에는 2,3번째 인자들은 쓸수도 안쓸수도 있는거라 실패.

# idea의 전환이 필요 경우의 수에 옷을 입지않는경우 (i + 1)을 미리해두고 나중에 아무것도 입지않은 수 -1 을 해주는것이 합리적.


# import collections

# def solution(clothes):
#    result = []
#    plus = 1
    
#    for i in range(len(clothes)):
#        result.append(clothes[i][1])
    
#    x = collections.Counter(result)

#    for i in x.values():
#        plus *= i

#    if len(x.keys()) == 1:
#        return len(clothes)
#    else:
#        return len(clothes) + plus


################################################
