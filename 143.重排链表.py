#
# @lc app=leetcode.cn id=143 lang=python3
#
# [143] 重排链表
#
from Tool.Python.ListNode import ListNode
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        nodes, node = [], head
        while node:
            nodes.append(node)
            node = node.next
        left, right, direction = 0, len(nodes) - 1, 0
        while left < right:
            l_node = nodes[left]
            r_node = nodes[right]
            direction += 1
            if direction % 2 == 1:
                l_node.next = r_node
                left += 1
            else:
                r_node.next = l_node
                right -= 1
            if left == right:
                nodes[left].next = None
        return head
# @lc code=end
print(Solution().reorderList(ListNode.build([1,2,3,4,5])))

