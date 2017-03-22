


'''
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.
'''
#Tip: Use DP, like complicated Fibonacci

def linked(c,k):
  return int(c[k-1:k+1])>10 and int(c[k-1:k+1])<=26 and int(c[k-1:k+1])!=20
def CodeWays(c):
  m=len(c)
  dp=[0 for i in range(m)]
  dp[0]=1
  dp[1]=2 if linked(c,1) else 1
  for i in range(2,m):
    dp[i]=dp[i-2]+dp[i-1] if linked(c,i) else dp[i-1]
    return dp
