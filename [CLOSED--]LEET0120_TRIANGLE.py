#coding=utf-8

#sum #O(N)space

"""
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
"""
def MinSum(t):
     LSum,CSum=t[0],[0]
     for i in range(1,len(t)):
          CSum[0]=LSum[0]+t[i][0]
          for j in range(1,len(LSum)):
               CSum[j]=t[i][j]+min(LSum[j],LSum[j-1])
          CSum.append(t[i][-1]+LSum[-1])
          LSum=CSum.copy()
     return min(CSum)
