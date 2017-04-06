#coding=utf-8

"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0
"""
def searchinsertposition(sortedlist,target):
    if target not in sortedlist:
        sortedlist.append(target)
        sortedlist.sort()
    return sortedlist.index(target)

"""
a more traditional solution
"""

def search(A, t):
    left,right,result=0,len(A)-1,0
    while left<=right:
        mid=left+int((right-left)/2)
        if A[mid]==t:
            return mid
        elif A[mid]>t:
            right,result=mid-1,mid
        else:
            left,result=mid+1,mid+1
            return result
