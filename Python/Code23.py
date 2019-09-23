# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from Python.Tool.ListNode import ListNode
class Solution:
    def mergeKLists(self, lists: [ListNode]) -> ListNode:
        listNodes = ListNode
        rootNode = None
        currentNode = None
        while len(listNodes) > 0:
            minNode = None
            for node in listNodes:
                if minNode == None:
                    minNode = node
                elif minNode.val > node.val:
                    minNode = node
            if minNode != None:
                listNodes.remove(minNode)
            if minNode.next != None:
                listNodes.append(minNode.next)
            if rootNode == None:
                rootNode = minNode
                currentNode = minNode
            else:
                currentNode.next = minNode
                currentNode = minNode
        return rootNode

Solution().mergeKLists([[1], [1,3,4], [2,6]])