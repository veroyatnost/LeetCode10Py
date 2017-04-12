#coding=utf-8

"""
Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.
"""
def plusOne(L):
  L[-1]+=1
  for i in reversed(range(1,len(L))):
    if L[i]==10:
      L[i]=0
      L[i-1]+=1
    if L[0]==10:
      L[0]=0
      L.insert(0,1)
  return L
