from Tool.Python.ListNode import ListNode

class Solution:
    def mergeKLists(self, lists: [ListNode]) -> ListNode:
        listNodes = []
        for list in lists:
            if type(list) == ListNode:
                listNodes.append(list)
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

# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# class Solution:
#     def mergeKLists(self, lists: [ListNode]) -> ListNode:
#         import heapq
#         dummy = ListNode(0)
#         p = dummy
#         head = []
#         for i in range(len(lists)):
#             if lists[i] :
#                 heapq.heappush(head, (lists[i].val, i))
#                 lists[i] = lists[i].next
#         while head:
#             val, idx = heapq.heappop(head)
#             p.next = ListNode(val)
#             p = p.next
#             if lists[idx]:
#                 heapq.heappush(head, (lists[idx].val, idx))
#                 lists[idx] = lists[idx].next
#         return dummy.next
# Solution().mergeKLists([[1], [1,3,4], [2,6]])
# Solution().mergeKLists([ListNode([1]), ListNode([1,3,4]), ListNode([2,6])])
Solution().mergeKLists([ListNode([]), ListNode([1,3,4]), ListNode([2,6])])