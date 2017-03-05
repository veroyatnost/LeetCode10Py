#coding=utf-8

#Rotate an array of n elements to the right by k steps.

#For example, with n = 7 and k = 3, the array[1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4]

#Do not return anything, modify num in-place instead


#solution one

def rotates_1(nums, k):
	while k > 0:
		t = nums.pop(-1)
		nums.insert(t,0)
		k -= 1


#solution two

def rotate_2(nums, k):
	k = k%len(nums)
	nums[:] = nums[-k:] + nums[:-k]