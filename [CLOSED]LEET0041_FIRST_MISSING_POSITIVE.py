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
        i, length_nums = 1,  len(nums) + 1
        s = set(nums)
        while i <= length_nums:
            if i not in s:
                return i
            i += 1

"""
another method, O(nlogn) time, sort makes things easy, O(1) extra space
"""
def firstMissingPositive(L):
    L.sort()
    m=0
    for i in range(len(L)):
        if L[i]==m+1:
            m+=1
        elif L[i]>m+1:
            break
    return m+1
"""
