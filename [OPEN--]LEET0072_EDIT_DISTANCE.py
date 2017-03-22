#coding=utf-8

"""
Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character
"""
def Conversion(w1,w2):
  m,n=len(w1),len(w2)
  dp=[[0 for i in range(n)] for j in range(m)]
  for i in range(n):
    dp[0][i]=i
  for i in range(m):
    dp[i][0]=i
    for j in range(1,n):
      dp[i][j]=1+min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1]) if w1[i]!=w2[j] else dp[i-1][j-1]
  return dp[m-1][n-1]
