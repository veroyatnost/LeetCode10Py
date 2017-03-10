#coding=utf-8

#Fibonacci #math #DP 

def Fibonacci(n):
    flast , fthis = 1, 1
    for i in range(2,n+1):
        fthis, flast = fthis+flast, fthis
    return fthis if n>=0 else None