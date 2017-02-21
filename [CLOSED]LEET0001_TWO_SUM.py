#coding=utf-8

'''
https://leetcode.com/problems/two-sum/?tab=Description
Given an array of integers, return indices of the two numbers such that 
they add up to a specific target.
you may not use the same element twice.
'''


def twoSum_1(nums, target):
    """
    :type nums: List[int] 
    :type target: int
    :rtype: List[int]
    """
    result = []
    n = len(nums)
    for i in range(n):
        for j in range(i+1,n):
            if target == nums[j] + nums[i]:
                result.append(i)
                result.append(j)
                return result
    return None


#solution 2
#base on hash

def twoSum_2(nums, target):
    dic = {}
    for index, num in enumerate(nums):
        if num in dic:
            return [dic[num], index]
        else:
            dic[target - num] = index