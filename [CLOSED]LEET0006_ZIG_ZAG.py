#coding=utf-8

def ZigZag(s, n):
    if n<3:
        return None
    m = n*2-2
    res = s[::m]
    for k in range(1,n-1):
        res += ''.join( [i+'' if j==None else j for i,j in map(None,s[k::m],s[m-k::m])])
    res += s[n-1::m]
    return res