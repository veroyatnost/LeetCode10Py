#coding=utf-8

'''
Given a string, sort it in decreasing roder based on the frequency of characters
'''

#solution one
#base the hash, count the characters and sort by frequency

def frequencySort_1(s):
	res, dic = '', {}
	for each in s:
		if each in dic:
			dic[each] += 1
		else:
			dic.setdefault(each, 1)
	dic_sort = sorted(dic.items(), key = lambda item:item[1], reverse= True)
	for char, frequency in dic_sort:
		res = res + char*frequency
	return res



#solution two
#call the API:collections

def frequencySort_2(s):
	import collections
	return ''.join(c*freq for c, freq in collections.Counter(s).most_common())