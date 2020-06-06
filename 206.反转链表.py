#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#
from Tool.Python.ListNode import ListNode
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        lastNode = None
        node = head
        while node != None:
            nodeNext = node.next
            node.next = lastNode
            lastNode = node
            if nodeNext != None:
                node = nodeNext
            else:
                head = node
                break
        return head
        # return None if head == None else reverse(None, head)

        # stack = []
        # while head != None:
        #     node = head
        #     ndoeNext = head.next
        #     node.next = None
        #     stack.append(node)
        #     head = ndoeNext
        # head = None
        # lastNode = None
        # while len(stack) > 0:
        #     node = stack.pop()
        #     if head == None:
        #         head = node
        #         lastNode = node
        #     else:
        #         lastNode.next = node
        #         lastNode = node
        # return head
# @lc code=end
print(Solution().reverseList(ListNode.node([1,2,3,4,5])))
