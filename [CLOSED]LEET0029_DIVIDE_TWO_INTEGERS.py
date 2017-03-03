#coding=utf-8

#number #bithack

MAX_INT = 2147483648

def divide_v0(dividend, divisor):
    if max(abs(dividend),abs(divisor))>MAX_INT or min(abs(dividend),abs(divisor))<1:
        return 0 if dividend==0 else None
    for i in range(32):
        if (divisor<<i) > dividend:
            break
    res, remain, i  = 0 , dividend, i-1
    while i >= 0 and (remain > ( divisor << i)) :
        print res, remain, i
        res , remain, i = res + (1 << i ) , remain - (divisor << i), i-1
    return res,remain