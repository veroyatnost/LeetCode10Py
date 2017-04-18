#coding=utf-8

"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

click to show follow up.

Follow up:
Did you use extra space?
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""

def setZeros(M):
  r=[0 in M[i] for i in range(len(M))]
  c=[0 in set(M[i][j] for i in range(len(M))) for j in range(len(M[0]))]
  for i in range(len(M)):
    for j in range(len(M[0])):
      M[i][j]=0 if r[i] or c[j] else M[i][j]
