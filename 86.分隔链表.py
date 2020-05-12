#
# @lc app=leetcode.cn id=86 lang=python3
#
# [86] 分隔链表
#
from Tool.ListNode import ListNode
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        small_queue = []
        max_queue = []
        node = head
        while node:
            if node.val < x:
                small_queue.append(node)
            else:
                max_queue.append(node)
            _node = node.next
            node.next = None
            node = _node
        head = None
        node = None
        while len(small_queue) > 0:
            _node = small_queue.pop(0)
            if head == None:
                head = _node
            else:
                node.next = _node
            node = _node
        while len(max_queue) > 0:
            _node = max_queue.pop(0)
            if head == None:
                head = _node
            else:
                node.next = _node
            node = _node
        return head
# @lc code=end
print(Solution().partition(ListNode.node([1,2,2]),3))