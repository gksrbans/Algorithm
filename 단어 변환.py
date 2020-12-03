# -*- conding: utf-8 -*-

'''
Author : gksrbans123@gmail.com
Date : 2020-12-03
URL : https://programmers.co.kr/learn/courses/30/lessons/43163
Type : DFS / BFS
'''


# 1. begin 에서 시작해서 한자리만 바뀐 words를 추림.
# 2. 거기에 target이 있으면 리턴, 없으면 DFS 들어감.
# 3. target을 찾을때 까지 반복진행 및 없으면 0 리턴 종료

# 문제는 한개만 차이나는 단어를 어케 추리냐임.
# 조합 combination 모듈을 꼭 써야할까 ? 싶음. (X)
# 한자리만 바꿀 수 있다 => len(words) - 1 만큼 조합. (X)
# List내 조건문을통해 자릿수 비교

import itertools


answer = 0

def DFS(begin, target, words, visit):
    global answer
    record = [begin]

    while record:
        temp = record.pop()

        if temp == target:
            return answer

        for i in range(0, len(words)):
            if len([j for j in range(len(words[i])) if words[i][j] != temp[j]]) == 1:
                if visit[i] != 0:
                    continue
                visit[i] = 1
                record.append(words[i])
        answer += 1

def solution(begin, target, words):
    if target not in words:
        return 0

    visit = [0 for _ in range(len(words))]
    DFS(begin, target, words, visit)
    return answer

