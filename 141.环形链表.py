#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#
from Tool.Python.ListNode import ListNode
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        quickNode = head
        slowNode = head
        run = False
        while True:
            if quickNode == None:
                return False
            if quickNode == slowNode and run == True:
                return True
            quickNode = quickNode.next
            if quickNode != None:
                quickNode = quickNode.next
            else:
                return False
            slowNode = slowNode.next
            run = True
        return False
# @lc code=end

