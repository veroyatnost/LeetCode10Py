#coding=utf-8

# version1
def findKthLargest(nums,k):
	'''
	:type nums: List[int]
	:type k: int
	:rtype: int
	'''
	return sorted(nums, reverse = True)[k-1]

# version2
from random import randint
def find_kth_largest(nums, k):
    # find a random pivot
    pivot = randint(0, len(nums) - 1)
    nums[pivot], nums[0] = nums[0], nums[pivot]

    # reorder so that left part > key, right part < key
    key, i = nums[0], 1
    for j in range(1, len(nums)):
        if nums[j] > key:
            nums[i], nums[j], i = nums[j], nums[i], i + 1
    nums[i - 1], nums[0] = nums[0], nums[i - 1]

    # divide and conqure
    return nums[i - 1] if i == k else \
           find_kth_largest(nums[i:], k - i) if i < k else find_kth_largest(nums[:i - 1], k)
