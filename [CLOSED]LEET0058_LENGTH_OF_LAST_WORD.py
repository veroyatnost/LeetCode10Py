#coding=utf-8

def LengthOfLast(s):
    lastlen = 0
    for c in s:
        lastlen = 0 if c=='' else (lastlen+1)
    return lastlen