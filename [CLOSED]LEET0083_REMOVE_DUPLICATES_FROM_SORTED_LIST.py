

'''
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
'''
def deleteDuplicates(head):
  if head==[]:
    return []
  current_index=1
  for i in range(1,len(head)):
    if head[current_index-1]!=head[i]:
      head[current_index]=head[i]
      current_index+=1
  return head[:current_index]
