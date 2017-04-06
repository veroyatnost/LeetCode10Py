"""
After robbing those houses on that street, the thief has found himself a new place for his thievery 
so that he will not get too much attention. This time, all houses at this place are arranged in a circle. 
That means the first house is the neighbor of the last one. Meanwhile, the security system for these houses remain 
the same as for those in the previous street. Given a list of non-negative integers representing the amount of money of each house,
determine the maximum amount of money you can rob tonight without alerting the police.
"""
def rob(L):
  if L==[]:
    return 0 
  elif len(L)==1 or len(L)==2:
    return max(L)
  def robS(L):
    dp=[0 for i in range(len(L))]
    dp[0],dp[1]=L[0],max(L[0],L[1])
    for i in range(2,len(L)):
      dp[i]=max(dp[i-1],dp[i-2]+L[i])
    return dp[-1]
  return max(robS(L[:-1]),robS(list(reversed(L[1:]))))
