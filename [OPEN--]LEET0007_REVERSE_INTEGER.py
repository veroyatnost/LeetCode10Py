#coding=utf-8

#Reverse digits of an integer.

#Example1: x = 123, return 321

#Example2: x = -123, return -321

def reverse(x):
	compare = (x > 0) - (x < 0)
    t = list(reversed(str(x*compare)))
    x = compare * int(''.join(i for i in t))
    return x if abs(x) < 2 ** 31 else 0