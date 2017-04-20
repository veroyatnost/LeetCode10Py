#coding=utf-8

#DP #

# Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

# For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
# the contiguous subarray [4,-1,2,1] has the largest sum = 6.
def maxSubArray(nums):
  MaxSum,Sum=nums[0],0
  for x in nums:
    if Sum > 0:
      Sum = Sum + x
    else:
      Sum = x
    if Sum > MaxSum:
      MaxSum=Sum
    return MaxSum   

  '''
  another method
  '''
  def maxSubArray(l):
    if l==[]:
      return 0
    sum,minSum,maxSum=l[0],min(0,l[0]),l[0]
    for i in range(1,len(l)):
      sum+=l[i]
      maxSum=max(maxSum,sum-minSum)
      minSum=min(minSum,sum)
    return maxSum
