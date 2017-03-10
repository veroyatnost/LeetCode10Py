#coding=utf-8
#version 1
def is_pal_number(x):
    if x < 0:
        return False

    rev, temp = 0, x
    while temp:
        rev = rev * 10 + temp % 10
        temp = temp // 10
    return rev == x

#version 2 in one line
IsPalNumber = lambda x:  str(x) == str(x)[::-1]
