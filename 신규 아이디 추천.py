# -*- conding: utf-8 -*-

'''
Author : gksrbans123@gmail.com
Date : 2021-02-13
URL : https://programmers.co.kr/learn/courses/30/lessons/72410
Type : 2021 카카오 kakakao
'''

def solution(new_id):
    new_id = new_id.lower()
    string = ""

    for i in new_id:
        if i.isalpha() or i.isdigit() or i == "-" or i == "_" or i == ".":
            string += i
        else:
            continue

    while '..' in string:
        string = string.replace('..', '.')
    print(string)
    if string[0] == ".":
        string = string[1:]

    if len(string)>= 1 and string[-1] == ".":
        string = string[:-1]

    if len(string) == 0:
        string = "a"

    if len(string) >= 16:
        string = string[:15]
        print(string[-1])
        if string[-1] == ".":
            string = string[:-1]

    if len(string) <= 2:
        while len(string) <= 2:
            string += string[-1]
    return string