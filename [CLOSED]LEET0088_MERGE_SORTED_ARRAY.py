


'''
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.
Do not return anything, modify nums1 in-place instead
'''
def merge(L1, m, L2, n):
  i,j,index=m-1,n-1,m+n-1
  while i>=0 and j>=0:
    if L1[i]>L2[j]:
      L1[index]=L1[i]
      i-=1
    else:
      L1[index]=L2[j]
      j-=1
    index-=1
  if j>=0:
    L1[:j+1]=L2[:j+1]
