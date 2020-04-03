# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from Python.ListNode import ListNode

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        while True:
            isNone = False
            node = head
            for i in range(k):
                if node == None:
                    isNone = True
                else:
                    node = node.next
                if isNone:
                    break
            if isNone:
                break
            pass


print(str(ListNode.node([1, 2, 3, 4, 5])))