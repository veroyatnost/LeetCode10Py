#coding=utf-8

#Given a collection of distinct numbers, return all possible permutations.

#For example
#[1,2,3] have the following permutations
#[
#[1,2,3],
#[1,3,2],
#[2,1,3],
#[2,3,1],
#[3,1,2],
#[3,2,1]
#]

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # result is the value that you should return
        result = []
        if len(nums) == 0:return result
        elif len(nums) == 1:return [nums]

        # use recursion which time complexity is n!(=n * (n - 1)!)
        else:
            for elem in nums:
                nums_copy = list(nums);nums_copy.remove(elem)
                lists = self.permute(nums_copy)
                for l in lists:
                    l_copy = list(l);l_copy.insert(0, elem);result.append(l_copy)
            return result
