#
# @lc app=leetcode.cn id=148 lang=python3
#
# [148] 排序链表
#
from Tool.Python.ListNode import ListNode
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        nodes = []
        node = head
        while node:
            nodes.append(node)
            node = node.next
        nodes.sort() # 用排序算法控制在O(n log n)
        res = None
        head = None
        for node in nodes:
            node.next = None
            if head == None:
                head = node
                res = node
            else:
                res.next = node
                res = res.next
        return head
# @lc code=end
print(Solution().sortList(ListNode.build([4,2,1,3])))
