"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements. 
For example, given nums  = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0]. 
Note:You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""

def moveZeroes(L):
  index=0
  for i in range(len(L)):
  if L[i]!=0:
    L[index]=L[i]
    index+=1
  for i in range(index,len(L)):
    L[i]=0
