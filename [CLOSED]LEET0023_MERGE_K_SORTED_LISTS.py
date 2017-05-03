#coding=utf-8
# Multi-way Merge Sort

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq as hq


def merge_k_lists(lists: List[ListNode]) -> ListNode:
    min_heap = []
    for node in lists:
        if node: hq.heappush(min_heap, (node.val, node))

    cur = head = ListNode(None)
    while len(min_heap) > 0:
        cur.next = hq.heappop(min_heap)[1]
        cur = cur.next
        if cur.next: hq.heappush(min_heap, (cur.next.val, cur.next))
    return head.next