#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#
from Python.ListNode import ListNode
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        node = head
        while node != None and node.next != None:
            if node.val != node.next.val:
                node = node.next
            else:
                node.next = node.next.next
        return head
# @lc code=end
print(Solution().deleteDuplicates(head=ListNode.node("1->1->2".split("->"))))
print(Solution().deleteDuplicates(head=ListNode.node("1->1->2->3->3".split("->"))))
