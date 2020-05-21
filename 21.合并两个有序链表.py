#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#
from Tool.ListNode import ListNode
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        headNode = None
        preNode = None
        while l1 != None or l2 != None:
            if l1 == None:
                if headNode == None:
                    headNode = l2
                if preNode != None:
                    preNode.next = l2
                preNode = l2
                l2 = l2.next
                preNode.next = None
            elif l2 == None:
                if headNode == None:
                    headNode = l1
                if preNode != None:
                    preNode.next = l1
                preNode = l1
                l1 = l1.next
                preNode.next = None
            else:
                if l1.val < l2.val:
                    if headNode == None:
                        headNode = l1
                    if preNode != None:
                        preNode.next = l1
                    preNode = l1
                    l1 = l1.next
                    preNode.next = None
                else:
                    if headNode == None:
                        headNode = l2
                    if preNode != None:
                        preNode.next = l2
                    preNode = l2
                    l2 = l2.next
                    preNode.next = None
        return headNode

# @lc code=end
print(Solution().mergeTwoLists(ListNode.node([1,2,4]), ListNode.node([1,3,4])))
