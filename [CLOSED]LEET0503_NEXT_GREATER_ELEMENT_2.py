#coding=utf-8
'''
https://leetcode.com/problems/next-greater-element-ii/?tab=Description
'''

def nextGreaterElements(nums):
    stack = []
    size = len(nums)
    ans = [-1]*size
    for x in range(size * 2):          #loop the nums list twice
        i = x % size
        while stack and nums[stack[-1]] < nums[i]:
            ans[stack.pop()] = nums[i]
        stack.append(i)
    return ans