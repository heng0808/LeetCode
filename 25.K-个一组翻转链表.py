#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#
from Tool.Python.ListNode import ListNode
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        root, pre_node = None, ListNode()
        l_node = head
        r_node = head
        count = 0
        while r_node != None:
            if count < k - 1:
                r_node = r_node.next
                count = count + 1
            else:
                pre_node.next, pre_node_next, r_node_next = r_node, l_node, r_node.next
                while l_node != r_node:
                    node = l_node
                    l_node = l_node.next
                    node.next = None
                    node.next = r_node.next
                    r_node.next = node
                if root == None:
                    root = pre_node.next
                pre_node = pre_node_next
                l_node, r_node = r_node_next, r_node_next
                count = 0
        return root
# @lc code=end
print(Solution().reverseKGroup(ListNode([1,2,3,4,5]), 1))

