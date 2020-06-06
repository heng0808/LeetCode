#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#
from Tool.Python.ListNode import ListNode
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = None
        preNode = None
        overNum = 0
        while l1 != None or l2 != None:
            val = overNum
            if l1 != None:
                val = val + l1.val
                l1 = l1.next
            if l2 != None:
                val = val + l2.val
                l2 = l2.next
            overNum = val // 10
            val = val % 10
            node = ListNode(val)
            if head == None:
                head = node
            else:
                preNode.next = node
            preNode = node
        if overNum > 0:
            preNode.next = ListNode(overNum)
        return head
# @lc code=end

