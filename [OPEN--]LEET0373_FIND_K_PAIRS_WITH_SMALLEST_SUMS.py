#coding=utf-8

#Given two integer arrays nums1 and nums2 sorted in ascending order and an integer k

#Define a pair (u,v) which consists of one element from the first array and one element

#from the second array. Find the k pairs(u1,v1),(u2,v2)...(uk,vk) with the smallest sums.

#Example:
#Given nums1 = [1,7,11], nums = [2,4,6], k = 3
#Return: [1,2],[1,4],[1,6]
#The first 3 pairs are returned from the sequence:
#[1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]

#Solution 1
def ksmallpairs_1(nums1, nums2, k):
	if nums1 == [] or nums2 == []: return []
    stack, res = [], []
    for item in nums1:
        for each in nums2:
            stack.append([each+item, item, each])
    keys = sorted(stack)[:k]
    for each in keys:
        res.append([each[1],each[2]])
    return res

 #Solution 2

 def ksmallpairs_2(nums1, nums2, k):
 	import itertools
 	import heapq
 	return map(list, heapq.nsmallest(k, itertools.product(nums1,nums2), key=sum))


#Solution 3

def ksmallpairs_3(nums1, nums2, k):
	import itertools
	import heapq
	streams = map(lambda u: ([u+v, u, v] for v in nums2), nums1)
	stream = heapq.merge(*streams)
	return [suv[1:] for suv in itertools.islice(stream, k)]
	