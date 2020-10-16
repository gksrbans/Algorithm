# -*- conding: utf-8 -*-

'''
Author : gksrbans123@gmail.com
Date : 2020-10-16 완료
URL : https://programmers.co.kr/learn/courses/30/lessons/42628
Type : Heap
'''

# 파이썬 heapQ는  최소힙만을 지원하기 때문에 최대힙에 대해서 어떻게 처리할건지 물어보는 문제 같음.
# 원큐에 통과하긴 했으나, 효율성 측면에서 채점되면 max,min 등을 사용해서 시간복잡도에서 통과가 안댈거 같음. (마지막에서만 써서 가능할 수도)
# 근데 문제는 최대, 최소힙원리로 풀긴 했는데, 내가봐도 허접함
# 최소힙, 최대힙을 저장하는 배열 두개를 만들어서 풀었음...

import heapq

def solution(operations):
    h = []
    max_h = []
    answer = []
    for i in operations:
        alphabet = i.split(" ")[0]
        number = int(i.split(" ")[-1])

        if alphabet == "I":
            heapq.heappush(h, number)
            heapq.heappush(max_h, (-number, number))

        elif alphabet == "D":
            try:
                if number < 0:
                    temp = heapq.heappop(h)
                    for i in range(len(max_h)):
                        if max_h[i][1] == temp:
                            max_h.pop(i)
                else:
                    temp = heapq.heappop(max_h)[1]
                    h.remove(temp)
            except:
                pass
    if not h:
        answer = [0,0]
    else:
        answer.append(max(h))
        answer.append(min(h))
    return answer


###################################################################

# 다른 사람 풀이
# class로 구현해서 직접 이진트리 함수 만든 애들 개쩌는거 같다;
# 하아ㅏㅏ

# import heapq
#
# REMOVED = "r"
#
#
# class DoublePriorityQueue:
#
#     def __init__(self):
#
#         self.entry_finder = {}
#         self.min_heap = []
#         self.max_heap = []
#         self.cnt = 0
#
#     def _check_empty(self, q) -> bool:
#         while q and q[0][1] == REMOVED:
#             heapq.heappop(q)
#         if not q:
#             return True
#         return False
#
#     def insert(self, v):
#         vid = self.cnt
#         min_ele, max_ele = [v, vid], [-v, vid]
#         heapq.heappush(self.min_heap, min_ele)
#         heapq.heappush(self.max_heap, max_ele)
#         self.entry_finder[vid] = [min_ele, max_ele]
#         self.cnt += 1
#
#     def pop_min(self):
#         is_empty = self._check_empty(self.min_heap)
#         if not is_empty:
#             value, vid = heapq.heappop(self.min_heap)
#             entries = self.entry_finder.pop(vid)
#             entries[1][1] = REMOVED
#
#     def pop_max(self):
#         is_empty = self._check_empty(self.max_heap)
#         if not is_empty:
#             value, vid = heapq.heappop(self.max_heap)
#             entries = self.entry_finder.pop(vid)
#             entries[0][1] = REMOVED
#
#     def get_min(self):
#         if not self._check_empty(self.min_heap):
#             return self.min_heap[0][0]
#         return 0
#
#     def get_max(self):
#         if not self._check_empty(self.max_heap):
#             return - self.max_heap[0][0]
#         return 0
#
#
# def solution(operations):
#     dpq = DoublePriorityQueue()
#
#     for each in operations:
#         op, num = each.split(" ")
#         num = int(num)
#         if op == "I":
#             dpq.insert(num)
#         elif op == "D" and num == -1:
#             dpq.pop_min()
#         else:
#             dpq.pop_max()
#
#     return [dpq.get_max(), dpq.get_min()]