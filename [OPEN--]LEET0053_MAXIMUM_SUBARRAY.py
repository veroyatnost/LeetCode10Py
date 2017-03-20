#coding=utf-8

#DP #

# Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

# For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
# the contiguous subarray [4,-1,2,1] has the largest sum = 6.
def maxSum(a):
  m,n,Min,Sum,Max=0,1,0,a[0],a[0]
  for i in range(1,len(a)):
    if Sum<Min:
      Min,m=Sum,i
      Sum+=a[i]
    if Sum-Min>Max:
      Max,n=Sum-Min,i+1
  return a[m:n]
