"""
Given two arrays, write a function to compute their intersection. 
Example: Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2]. 
Note:Each element in the result must be unique.The result can be in any order.
"""

import bisect as bs
def intersection(L1,L2):
  if L2==[]:
    return []
  L2.sort()
  R=[]
  for n in set(L1):
    i=bs.bisect_left(L2,n)
    if i!=len(L2) and n==L2[i]:
      R.append(n)
  return R
