"""
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
Find all the elements of [1, n] inclusive that do not appear in this array.Could you do it without extra space and in O(n) runtime? 
You may assume the returned list does not count as extra space.
Example: Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]


"""

L.insert(0,0)
  L.sort()
  NL=[]
  for i in range(1,len(L)):
    if L[i]-L[i-1]>1:
      for j in range(L[i-1]+1,L[i]):
        NL.append(j)
  if L[-1]<len(L)-1:
    for i in range(L[-1]+1,len(L)):
      NL.append(i)
  return NL
