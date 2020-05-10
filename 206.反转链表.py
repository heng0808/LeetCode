#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#
from Tool.ListNode import ListNode
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def reverse(lastNode, node) -> ListNode:
            if node.next == None:
                node.next = lastNode
                return node
            else:
                nextNode = node.next
                node.next = lastNode
                return reverse(node, nextNode)
        return None if head == None else reverse(None, head)

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
