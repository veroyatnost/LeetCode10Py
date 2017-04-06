#coding=utf-8

# Given an array of non-negative integers, you are initially positioned at the first index of the array.

# Each element in the array represents your maximum jump length at that position.

# Determine if you are able to reach the last index.

# For example:

# A = [2,3,1,1,4], return true.

# A = [3,2,1,0,4], return false.
def canJump(self, l):
  furthest=0
  index=0
  while index<=furthest and index<len(l):
    furthest=max(furthest,index+l[index])
    index+=1
  return index==len(l)
