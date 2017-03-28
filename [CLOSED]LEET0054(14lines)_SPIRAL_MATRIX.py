#coding=utf-8

# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

# For example,

# Given the following matrix:
def Spiral(m):    
  if m==[]:        
    return []
  dire,index,R,C,lis=((0,1),(1,0),(0,-1),(-1,0)),0,0,0,[]
  currDir=dire[index]
  for i in range(len(m)*len(m[0])):
    lis.append(m[R][C])
    m[R][C]=False
    if R+currDir[0]<0 or C+currDir[1]<0 or R+currDir[0]>=len(m) or C+currDir[1]>=len(m[0]) or m[R+currDir[0]][C+currDir[1]]==False:
      index+=1
      currDir=dire[index%4]
    R+=currDir[0]
    C+=currDir[1]
  return lis
