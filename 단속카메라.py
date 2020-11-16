# -*- conding: utf-8 -*-

'''
Author : gksrbans123@gmail.com
Date : 2020-11-14
URL : https://programmers.co.kr/learn/courses/30/lessons/42884
Type : Greedy
'''

def solution(routes):
    ENTER, EXIT, N = 0, 1, len(routes)
    routes = sorted(routes, key = lambda x:x[1])
    check = [False] * N
    #print(routes)
    #print(check)
    camera, count = -30000, 0

    for i in range(N):
        if check[i]:
            continue
        count += 1
        camera = routes[i][EXIT]
        for i in range(i, N):
            if routes[i][ENTER] <= camera and camera <= routes[i][EXIT]:
                check[i] = True

    return count

##########################################################################
# Refer : https://velog.io/@tjdud0123/%EB%8B%A8%EC%86%8D-%EC%B9%B4%EB%A9%94%EB%9D%BC