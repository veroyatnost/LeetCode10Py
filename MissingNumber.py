#coding=utf-8

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for elements in range(len(nums)+1):
            if elements not in nums:
                return elements
