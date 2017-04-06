"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, 
the only constraint stopping you from robbing each of them is that adjacent houses have security system connected 
and it will automatically contact the police if two adjacent houses were broken into on the same night.
Given a list of non-negative integers representing the amount of money of each house, 
determine the maximum amount of money you can rob tonight without alerting the police.

"""
def rob(L):
  if L==[]:
    return 0
  elif len(L)==0:
    return L[0]
  dp=[0 for i in range(len(L))]
  dp[0],dp[1]=L[0],max(L[0],L[1])
  for i in range(2,len(L)):
    dp[i]=max(dp[i-1],dp[i-2]+L[i])
  return dp[-1]
