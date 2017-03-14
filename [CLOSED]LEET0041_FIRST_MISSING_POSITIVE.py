#coding = utf-8

#Given an unsorted integer array, find the first missing positive integer.

#for example
#Given [1,2,0] return 3,
#and [3,4,-1,1] return 2

#Your algorithm should run in O(n) time and uses constant space.

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, length_nums = 0,  len(nums) + 1
        s = set(nums)
        while i <= length_nums:
            i += 1
            if i not in s:
                return i
