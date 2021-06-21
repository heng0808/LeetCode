#
# @lc app=leetcode.cn id=86 lang=python3
#
# [86] 分隔链表
#
from Tool.Python.ListNode import ListNode
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        pre_left, left, right = None, head, head
        while right and right.next:
            right = right.next
        head, foot = None, None
        while left != right:
            leftNext = left.next
            if left.val >= x:
                left.next = None
                if foot == None:
                    right.next = left
                    foot = left
                    right = right.next
                else:
                    foot.next = left
                    foot = foot.next
                if pre_left != None:
                    pre_left.next = leftNext
            else:
                pre_left = left
                if head == None:
                    head = left
            left = leftNext
        if head == None:
            head = left
        return head
                
# @lc code=end
print(Solution().partition(ListNode.build([1,2]),3))