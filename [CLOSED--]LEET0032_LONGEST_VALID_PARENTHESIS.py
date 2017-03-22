#coding=utf-8

#list

"""
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.

Subscribe to see which companies asked this question.
"""

# Hint: CumSum, two-cursor, DP O(MN)
def Paren(s,i):
  return s[i-1:i+1]=='()'
def ParenNum(s):
  m=len(s)
  dp=[0 for i in range(m)]
  dp[0]=0
  dp[1]=1 if Paren(s,1) else 0
  for i in range(2,m):
    dp[i]=dp[i-2]+1 if Paren(s,i) else dp[i-1]
  return dp[m-1]
