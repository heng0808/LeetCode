# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from Tool.ListNode import ListNode

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None and l2 == None:
            return None
        elif l1 == None:
            return l2
        elif l2 == None:
            return l1
        else:
            l1Node = l1
            l2Node = l2
            rootNode = None
            node = None
            if l1Node.val < l2Node.val:
                rootNode = l1Node
                node = l1Node
                l1Node = l1Node.next
            else:
                rootNode = l2Node
                node = l2Node
                l2Node = l2Node.next

            while l1Node != None or l2Node != None:
                if l1Node == None:
                    node.next = l2Node
                    node = node.next
                    l2Node = l2Node.next
                elif l2Node == None:
                    node.next = l1Node
                    node = node.next
                    l1Node = l1Node.next
                else:
                    if l1Node.val < l2Node.val:
                        node.next = l1Node
                        node = node.next
                        l1Node = l1Node.next
                    else:
                        node.next = l2Node
                        node = node.next
                        l2Node = l2Node.next
            return rootNode

node1 = ListNode.node("124")
node2 = ListNode.node("134")
node = Solution().mergeTwoLists(node1, node2)
pass
