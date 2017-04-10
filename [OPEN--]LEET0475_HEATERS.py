


'''
Winter is coming! Your first job during the contest is to design a standard heater with fixed warm radius to warm all the houses.

Now, you are given positions of houses and heaters on a horizontal line, find out minimum radius of heaters so that all houses could be covered by those heaters.

So, your input will be the positions of houses and heaters seperately, and your expected output will be the minimum radius standard of heaters.

Note:
1.Numbers of houses and heaters you are given are non-negative and will not exceed 25000.
2.Positions of houses and heaters you are given are non-negative and will not exceed 10^9.
3.As long as a house is in the heaters' warm radius range, it can be warmed.
4.All the heaters follow your radius standard and the warm radius will the same.
Example:
Input: [1,2,3],[2]
Output: 1
Explanation: The only heater was placed in the position 2, and if we use the radius 1 standard, then all the houses can be warmed.
'''

def findRadius(houses, heaters):
	hou, heat, max_dis, i, j = sorted(houses), sorted(heaters), 0, 0, 0
	while i < len(hou):
		if j < len(heat)-1 and heat[j+1] - hou[i] <= hou[i] - heat[j]:
			j += 1
		else:
			max_dis = max(max_dis, abs(heat[i]-hou[j]))
			i += 1
		return max_dis
