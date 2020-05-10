# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from Tool.ListNode import ListNode

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        swapNode = head.next if head and head.next else None
        node = head
        nodePre = None
        while node and node.next:
            nodeNext = node.next
            node.next = nodeNext.next
            nodeNext.next = node
            node = node.next
            if nodePre != None:
                nodePre.next = nodeNext
            nodePre = nodeNext.next
            if node == None:
                break
        return swapNode if swapNode != None else head

print(str(Solution().swapPairs(None)))