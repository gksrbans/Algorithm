# -*- conding: utf-8 -*-

'''
Author : gksrbans123@gmail.com
Date : 2021-03-08
URL : https://programmers.co.kr/skill_checks/257169
Type : 스킬을 체크해보자
'''

from collections import defaultdict


genres, plays = ["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]
answer= []
genre_dict = defaultdict(lambda: 0)

for g, p in zip(genres, plays):
    genre_dict[g] += p

print(genre_dict)

genre_dict = sorted(genre_dict.items(), key=(lambda x: x[1]), reverse=True)
print(genre_dict, 't')

dict = defaultdict(lambda: [])

for i, tuple in enumerate(zip(genres, plays)):
    dict[tuple[0]].append((tuple[1], i))
print(dict)
for genre in genre_dict:
    print(genre, 't')
    list = sorted(dict[genre[0]], key=(lambda x: x[0]), reverse=True)
    if len(list) > 1:
        answer.append(list[0][1])
        answer.append(list[1][1])
    elif len(list) == 1:
        answer.append(list[0][1])

print(answer)

