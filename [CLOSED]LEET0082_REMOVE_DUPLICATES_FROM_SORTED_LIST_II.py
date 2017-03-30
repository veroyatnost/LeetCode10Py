

'''
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
'''
def deleteDuplicates(l):
  if l==[]:
    return []
  l=[False]+l+[False]
  index=1
  for i in range(1,len(l)-1):
    if l[i]!=l[i-1] and l[i]!=l[i+1]:
      l[index]=l[i]
      index+=1
  return l[1:index]
