#coding=utf-8

#Given an array of non-negative integers, you are initially positioned at the first index of the array.

#Each element in the array represents your maximum jump length at that position.

#Your goal is to reach the last index in the minimum number of jumps.

#For example:
#Given array A = [2,3,1,1,4]
#The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)

def jump(L):
  dp=[i for i in range(len(L))]
  for i in range(1,len(L)):
    for j in range(i):
      if L[j]+j>=i dp[j]+1<dp[i]:
        dp[i]=min(dp[j]+1,dp[i])
  return dp[-1]
