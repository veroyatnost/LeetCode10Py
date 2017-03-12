#coding=utf-8

#math #pascaltriangle #combinations #follow0118

"""
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?

"""
import scipy.special as ssp

#Version 0: From Leet0118
def PascalTriangleLastRow_v0(N):
    res = [[1]]
    for i in range(1,N+1):
        lastrow = res[-1]
        newrow = [1]+[lastrow[j]+lastrow[j+1] for j in range(len(lastrow)-1)]+[1]
        res.append(newrow)
    return res[-1] if N>=1 else None

##Version 1: From Leet0119
def PascalTriangleLastRow_v1(N):
    lastrow = [1]
    for i in range(1,N+1):
        lastrow = [1]+[lastrow[j]+lastrow[j+1] for j in range(len(lastrow)-1)]+[1]
    return lastrow if N>=1 else None


PscalTriangleLastRow_v9 = lambda N: [int(ssp.comb(N,i)) for i in range(N+1)] if N>=1 else None
