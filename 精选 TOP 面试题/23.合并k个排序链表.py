#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个排序链表
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        k_heap=[]
        for i in lists:
            while i:
                k_heap.append(i.val)
                i=i.next
        if k_heap==[]:
            return []
        k_heap.sort()
        head=cur=ListNode(0)
        while k_heap:
            cur.next=ListNode(k_heap.pop(0))
            cur=cur.next
        return head.next
