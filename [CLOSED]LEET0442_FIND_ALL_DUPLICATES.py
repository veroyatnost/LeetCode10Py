#coding=utf-8

'''
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array),
some elements appear twice and others appear once
find duolicate elements
'''

#solution One
#use Counter, transform into dict

def findDuplicates_1(nums):
    from collections import Counter
    result =[]
    c = dict(Counter(nums))
    for key, val in c.items():
        if val == 2：
            result.append(key)
    return result


#solution Two
#Use arry itself as hash map, the same element will map same result
#Due to 1 ≤ a[i] ≤ n (n = size of array), a[i]-1 represent index
#when first element map, the result * -1, the nums's elements will change, 
#so add abs() --> abs(a[i]-1) that do not change the nums's index
#when arrived the later same elments, the map result is smaller than 0

def findDuplicates_2(nums)
	res = []
	for x in nums:
		if nums[abs(x) - 1] <0:   
			res.append(abs(x))
		else:
			nums[abs(x) - 1 ] *= -1
	return res