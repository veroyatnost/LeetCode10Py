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
