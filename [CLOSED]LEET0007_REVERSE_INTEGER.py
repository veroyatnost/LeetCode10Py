#coding=utf-8
"""
0007 and 0009 are similar while solving one of them could refer to the other one.
"""

#Reverse digits of an integer.

#Example1: x = 123, return 321

#Example2: x = -123, return -321

#version 1
def reverse(x):
	compare = (x > 0) - (x < 0)
    t = list(reversed(str(x*compare)))
    x = compare * int(''.join(i for i in t))
    return x if abs(x) < 2 ** 31 else 0

#version 2
def reverse2(x):
	return int(str(x)[::-1] if x>0 else "-"+(str(abs(x))[::-1]))

#version 3
reverseLambda = lambda x: int(str(x)[::-1] if x>0 else "-"+(str(abs(x))[::-1]))
