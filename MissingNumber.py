#coding=utf-8

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return (set(range(len(nums)+1)) - set(nums)).pop()
