"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
Find the minimum element.You may assume no duplicate exists in the array.

"""
def search(nums):
  l,r=0,len(nums)-1
  while l<r:
    m=l+int((r-l)/2)
    if nums[m]<nums[r]:
      r=m
    elif nums[m]>nums[r]:
      l=m+1
  return nums[l]
