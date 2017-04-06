#coding=utf-8

"""
Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.
"""
def sortColors(l):
  index0,index2=0,len(l)-1
  for i in range(len(l)):
    if l[i]==0:
      l[index0],l[i]=l[i],l[index0]
      index0+=1
  for i in reversed(range(index0,len(l))):
    if l[i]==2:
      l[index2],l[i]=l[i],l[index2]
      index2-=1
