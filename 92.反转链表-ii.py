#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#
from Tool.Python.ListNode import ListNode
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        pre_node, node, index = None, head, 1
        while True:
            if index == m:
                if pre_node:
                    pre_node.next = None
                swap_pre_node, swap_node, swap_index = None, node, index
                while swap_node and swap_index <= n:
                    next_node = swap_node.next
                    next_pre_node = swap_node
                    next_pre_node.next = None
                    if swap_pre_node:
                        swap_node.next = swap_pre_node
                    swap_pre_node = next_pre_node
                    swap_node = next_node
                    swap_index += 1
                if swap_node:
                    node.next = swap_node
                if pre_node:
                    pre_node.next = swap_pre_node                
                if not pre_node:
                    head = swap_pre_node
                break
            index += 1
            pre_node = node
            node = node.next
        return head
# @lc code=end

print(Solution().reverseBetween(ListNode([1,2,3,4,5]), 1, 8))

