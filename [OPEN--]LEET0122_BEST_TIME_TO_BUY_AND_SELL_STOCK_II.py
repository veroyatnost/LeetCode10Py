


'''
Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). 
However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
'''
def maxProfit(prices):
	if not prices: return 0
	i, n, res = 0, len(prices)-1, 0
	while i < n:
		if prices[i] < prices[i+1]:
			res = res + prices[i+1] - prices[i]
		i+=1
	return res