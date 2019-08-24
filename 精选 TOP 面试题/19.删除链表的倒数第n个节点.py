#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第N个节点
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        second = fist = head
        for i in range(n):  # 第一个指针先走 n 步
            fist = fist.next
 
        if fist == None:  # 如果现在第一个指针已经到头了，那么第一个结点就是要删除的结点。
            return second.next
 
        while fist.next:  # 然后同时走，直到第一个指针走到头
            fist = fist.next
            second = second.next
        second.next = second.next.next  # 删除相应的结点
        return head
