#coding=utf-8

#list #inplace #two_cursor

"""
Given an array and a value, remove all instances of that value in place and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example:
Given input array nums = [3,2,2,3], val = 3

Your function should return length = 2, with the first two elements of nums being 2.
"""

# nums = [3,2,2,3]
# nums = [2,2,2,2]
# nums = [3,3,3,3]
# nums = [3,2,2,2]


def remove_inplace(nums, value):
    """
    {Complexity: {Time:O(N),Space:O(1)}}
    """
    start, end = 0, len(nums)-1
    while start <= end:
        if nums[end]==value:
            end-=1
        elif nums[start]!=value:
            start+=1
        else:
            nums[start],nums[end] = nums[end],nums[start]
    return end+1