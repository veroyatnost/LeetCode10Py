

'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.
'''


#Tag:123 DP, a[i,k] which means i th day. k=1,2, means the first order or the second order, derive from a[i-1,k] and a[i-1,k-1]
