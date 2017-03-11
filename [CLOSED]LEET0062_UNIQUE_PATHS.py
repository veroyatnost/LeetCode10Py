#coding=utf-8

#combinations

def UniquePaths(m,n):
    res = 1
    for i in range(n-1):
        res = res*(m+i)/(i+1)
    return res
        