#coding=utf-8

"""
Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character
"""
def minDistance(word1,word2):
  m,n=len(word1),len(word2)
  dp=[[0 for j in range(n+1)] for i in range(m+1)]
  for i in range(n+1):
    dp[0][i]=i
  for i in range(1,m+1):
    dp[i][0]=i
    for j in range(1,n+1):
      dp[i][j]=1+min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1]) if word1[i-1]!=word2[j-1] else dp[i-1][j-1]
  return dp[m][n]
