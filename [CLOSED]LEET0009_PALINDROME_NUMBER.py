#coding=utf-8
"""
0007 and 0009 are similar while solving one of them could refer to the other one

version 1 of IsPalNumber using the basic way to solve 0009. However, PALINDROME NUMBER
could be taken as string or even list. Int is not necessary.

"""

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
