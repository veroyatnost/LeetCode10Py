#coding = utf-8

#You are given an n x n 2D matrix representing an image.

#Rotate the image by 90 degrees (clockwise).

#Could you do this in-place?
def rotate(m):
  n=len(m)
  for i in range(int(n/2)):
    for j in range(i,n-i-1):
      temp1,temp2,temp3,temp4=m[i][j],m[j][n-1-i],m[n-1-i][n-1-j],m[n-1-j][i]
      m[i][j],m[j][n-1-i],m[n-1-i][n-1-j],m[n-1-j][i]=temp4,temp1,temp2,temp3
