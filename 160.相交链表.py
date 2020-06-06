#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#
from Tool.Python.ListNode import ListNode
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lengthA = 0
        nodeA = headA
        while nodeA != None:
            nodeA = nodeA.next
            lengthA = lengthA + 1

        lengthB = 0
        nodeB = headB
        while nodeB != None:
            nodeB = nodeB.next
            lengthB = lengthB + 1

        nodeA = headA
        nodeB = headB
        if lengthA > lengthB:
            while lengthA > lengthB:
                nodeA = nodeA.next
                lengthA = lengthA - 1
        elif lengthB > lengthA:
            while lengthB > lengthA:
                nodeB = nodeB.next
                lengthB = lengthB - 1

        while nodeA != None and nodeB != None:
            if nodeA == nodeB:
                return nodeA
            else:
                nodeA = nodeA.next
                nodeB = nodeB.next
        return None
# @lc code=end

