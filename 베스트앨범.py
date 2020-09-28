# -*- conding: utf-8 -*-

'''
Author : gksrbans123@gmail.com
Date : 2020-09-28
URL : https://programmers.co.kr/learn/courses/30/lessons/42579
Type : Hash
'''

from collections import defaultdict
from operator import itemgetter

def solution(genres, plays):
    g_p_dict = defaultdict(lambda: 0)
    
    for g, p in zip(genres, plays):
        g_p_dict[g] += p
        
    #print(g_p_dict)
    g_p_sort = [x for x, y in sorted(g_p_dict.items(), key=itemgetter(1), reverse=True)]
    #print(g_p_sort)
    
    final_dict = defaultdict(lambda: [])
    
    for i, tuple in enumerate(zip(genres, plays)):
        final_dict[tuple[0]].append((tuple[1], i))
    
    answer = []
    for genre in g_p_sort:
        list = sorted(final_dict[genre], key=itemgetter(0), reverse=True)
        if len(list) > 1:
            answer.append(list[0][1])
            answer.append(list[1][1])
        elif len(list) == 1:
            answer.append(list[0][1])
    return answer

# itemgetter 메서드에 대해서 알게되었다. lambda 표현식보다 효율이 좋다고 한다.
# 전반적인 생각들은 비슷했는데, dict에 튜플을 집어넣을준 몰랐다.
# dict 내 튜플에 값과 인덱스를 둘다 집어넣고 가져다 쓴다.

# kata님의 게시글 참조하였다.
# https://somjang.tistory.com/entry/Programmers-%ED%95%B4%EC%8B%9C-%EB%B2%A0%EC%8A%A4%ED%8A%B8%EC%95%A8%EB%B2%94-Python






# 첫 번째 제출 코드.
# 모든 장르는 재생된 횟수가 다릅니다. 를 다르게 해석했었다. 같은 장르에서는 같은 play 횟수가 나오는 실패 테스트 케이스 발생함.
# Ex) ["classic", "classic", "classic", "classic", "pop"], [500, 150, 800, 800, 2500]
# 86.7 점 테스트케이스 2개 실패.
'''
from collections import defaultdict
from operator import itemgetter

def solution(genres, plays):
    g_p_dict = defaultdict(lambda: 0)
    
    for g, p in zip(genres, plays):
        g_p_dict[g] += p
        
    #print(g_p_dict)
    g_p_sort = [x for x, y in sorted(g_p_dict.items(), key=itemgetter(1), reverse=True)]
    #print(g_p_sort)
    
    final_dict = defaultdict(lambda: [])
    
    for i, tuple in enumerate(zip(genres, plays)):
        final_dict[tuple[0]].append((tuple[1], i))
    
    answer = []
    for genre in g_p_sort:
        list = sorted(final_dict[genre], key=itemgetter(0), reverse=True)
        if len(list) > 1:
            answer.append(list[0][1])
            answer.append(list[1][1])
        elif len(list) == 1:
            answer.append(list[0][1])
    return answer
'''
    
    
