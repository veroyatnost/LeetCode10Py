#coding=utf-8

#math #pascaltriangle #combinations

"""
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""

def PascalTriangle_v0(N):
    res = [[1]]
    for i in range(2,N+1):
        lastrow = res[-1]
        newrow = [1]+[lastrow[j]+lastrow[j+1] for j in range(len(lastrow)-1)]+[1]
        res.append(newrow)
    return res if N>=1 else None