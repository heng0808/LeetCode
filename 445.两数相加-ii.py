#
# @lc app=leetcode.cn id=445 lang=python3
#
# [445] 两数相加 II
#
from Tool.Python.ListNode import ListNode
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1 = []
        stack2 = []
        while l1 or l2:
            if l1:
                stack1.append(l1.val)
                l1 = l1.next
            if l2:
                stack2.append(l2.val)
                l2 = l2.next

        r = ListNode(val = 0)

        while True:
            if len(stack1) > 0:
                r.val += stack1.pop()
            if len(stack2) > 0:
                r.val += stack2.pop()
            if len(stack1) == 0 and len(stack2) == 0:
                if r.val > 9:
                    r.val -= 10
                    r = ListNode(val = 1, next = r)
                break
            else:
                if r.val > 9:
                    r.val -= 10
                    r = ListNode(val = 1, next = r)
                else:
                    r = ListNode(val = 0, next = r)
        return r
# @lc code=end
print(Solution().addTwoNumbers(ListNode.build([7,2,4,3]), ListNode.build([5,6,4])))