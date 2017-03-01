#coding=utf-8

def findKthLargest(nums,k):
	'''
	:type nums: List[int]
	:type k: int
	:rtype: int
	'''
	return sorted(nums, reverse = True)[k-1]