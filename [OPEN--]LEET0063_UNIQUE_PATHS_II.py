#coding=utf-8

#DP

"""
Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.

Note: m and n will be at most 100.
"""
def uniquePathsWithObstacles(obstacleGrid):
  m,n=len(obstacleGrid),len(obstacleGrid[0])
  dp=[[0 for i in range(n)] for i in range(m)]
  for j in range(n):
    #time inefficiency
    dp[0][j]=1 if obstacleGrid[0][:j+1].count(1)==0 else 0
  for i in range(1,m):
    dp[i][0]=1 if list(zip(*obstacleGrid))[0][:i+1].count(1)==0 else 0
    for j in range(1,n):
      dp[i][j]=dp[i-1][j]+dp[i][j-1] if obstacleGrid[i][j]==0 else 0
  return dp[m-1][n-1]
