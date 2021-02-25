# -*- conding: utf-8 -*-

'''
Author : gksrbans123@gmail.com
Date : 2021-02-26
URL : https://programmers.co.kr/skill_checks/252929
Type : 스킬을 체크해보자
'''

gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]

TYPE_NUM = len(set(gems))
GEM_NUM = len(gems)
cur_shop = {gems[0]: 1}
cand = []
l_idx, r_idx = 0, 0
DIST, RESULT = 0, 1

while l_idx < GEM_NUM and r_idx < GEM_NUM:
    if len(cur_shop) < TYPE_NUM:
        r_idx += 1
        if r_idx == GEM_NUM:
            break
        cur_shop[gems[r_idx]] = cur_shop.get(gems[r_idx], 0) + 1
    else:
        cand.append((r_idx - l_idx, [l_idx + 1, r_idx + 1]))
        cur_shop[gems[l_idx]] -= 1
        if cur_shop[gems[l_idx]] == 0:
            del cur_shop[gems[l_idx]]
        l_idx += 1
print(cur_shop)
print(cand)