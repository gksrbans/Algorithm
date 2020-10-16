# -*- conding: utf-8 -*-

'''
Author : gksrbans123@gmail.com
Date : 2020-10-15 // (재도전) // 2020-10-16 완료
URL : https://programmers.co.kr/learn/courses/30/lessons/42627
Type : Heap
'''

import heapq

def solution(jobs):
    h = []
    jobs = sorted(jobs, key=lambda x:x[1])
    Range = len(jobs)
    count = 0
    end = -1 # 첫 번째 루프를 통과시키기 위해 -1로 시작.

    answer = 0
    time = 0

    while count < Range: # 루프문을 어떻게 돌릴 생각하는게 중요한거 같음...
        for x, y in jobs:
            if end < x <= time: # 시작 시간과 종료 시간을 가지고 힙에 넣을 거라고 생각하기
                heapq.heappush(h, (y,x))
                #print(h)

        if len(h) > 0: # 힙 안에 들어갔으면 들어가는 조건문
            count += 1 # 힙 안에 들어왔으니까 카운팅 증가 시킴( 루프문 자체가 카운트로 동작함 )
            end = time # 끝나는 시간을 현재 시간으로 바꿔줌
            term, start = heapq.heappop(h) # 힙 에서 레코드를 제거함과 동시에 변수로 얼마나 걸리는 job인지의 Term 과 그 작업이 시작한 시간 start를 변수에 담음
            time += term # time에서 작업이 걸린 시간을 더해줌
            answer += (time - start) # 결국 찾아야 할 답은 총걸린 시간에서 시작시간 빼주면 job이 진행되는 시간인 answer를 변수에 차곡 차곡 더해준다고 생각하면 됨.
        else:
            time += 1 # 힙 안에 넣을 수없는 경우 시간만 증가시키고 while 처음으로 돌아감
    return answer//Range

# 계속 뭔가 해보다가 안대서 레퍼런스 참고했음 ㅠㅠ
# Refer : https://seoyoung2.github.io/algorithm/2020/06/04/Programmers-diskcontroller.html

# 다시할거임 아ㅏㅏㅏ나ㅏㅏㅏㅏ

# import heapq
#
# def solution(jobs):
#     jobs.sort()
#     h = []
#     index = [0]
#     index2 = [0]
#
#     for i in jobs:
#         heapq.heappush(h, (i[1], i[0]))
#
#     for i in range(len(h)):
#         temp = heapq.heappop(h)
#         print(temp)
#         index.append(index[-1] + temp[0])
#
#         if index[-1] > temp[1]:
#             index2.append(temp[1])
#         else:
#             index2.append(0)
#     for i in range(len(index)):
#         index[i] = index[i] - index2[i]
#
#     answer = sum(index) // len(jobs)
#     return answer
