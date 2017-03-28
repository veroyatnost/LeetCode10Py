#coding=utf-8

"""
Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""
def generateMatrix(n):
  m=[[0 for i in range(n)] for i in range(n)]
  dire,index,R,C,num=((0,1),(1,0),(0,-1),(-1,0)),0,0,0,1
  currDir=dire[index]
  for i in range(n*n):
    m[R][C]=num
    num+=1
    if R+currDir[0]<0 or C+currDir[1]<0 or R+currDir[0]>=len(m) or C+currDir[1]>=len(m[0]) or m[R+currDir[0]][C+currDir[1]]!=0:
      index+=1
      currDir=dire[index%4]
    R+=currDir[0]
    C+=currDir[1]
  return m
