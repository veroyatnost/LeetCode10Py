#coding=utf-8

'''
Given a string S, you are allowed to convert it to a palindrome by adding
characters in front of it. Find and return the shortest.
'''

def shortestPalindrom(s):
	n = len(s)
	l, r = n/2, (n+1)/2
	while l > 0:
		if s[:l] == s[r+l-1: r-1: -1]: break
		elif l == r: l -= 1
		else :	r -= 1

	left_pal = s[n-1: l+r -1 : -1]
	return left_pal + s

