def twoSum(nums, target):
    """
    :type nums: List[int] 
    :type target: int
    :rtype: List[int]
    Given an array of integers, return indices of the two numbers such that 
    they add up to a specific target.
    You may assume that each input would have exactly one solution, 
    and you may not use the same element twice.
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