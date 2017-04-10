#coding = utf-8


'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.
'''

#use break force, time: O(n) 

def findMin_v0(nums):
	for i in range(len(nums)-1):
		if nums[i+1] < nums[i]: return nums[i+1]
	return nums[0]


#use binary search, time:O(logn)

def findMin_v1(nums):
	l, r = 0, len(nums) - 1
	while l < r:
		mid = l + int((r - l)/2)
		if nums[mid] < nums[r]:
			r = mid
		else:
			l = mid + 1
	return nums[l]

#Use built-in function min()
def findMin_v2(nums):
	return min(nums)


#Use built-in function sorted()
def findMin_v3(nums):
	return sorted(nums)[0]