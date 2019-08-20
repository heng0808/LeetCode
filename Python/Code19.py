# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        count = 0
        noderight = None
        nodeleft = head
        while True:
            if n == 0:
                break
            else:
                n = n - 1
            if noderight:
                noderight = noderight.next
            else:
                noderight = head.next
        if noderight == None:
            return head.next
        while True:
            if noderight.next == None:
                nodeleft.next = nodeleft.next.next
                break
            else:
                nodeleft = nodeleft.next
                noderight = noderight.next
        return head
# 1->2->3->4->5
# 1->2->3->5
# 1->2->3->4->5
# l->x->r
#       l->x->r
# noderoot = ListNode(1)
# _node = noderoot
# for i in range(2, 6):
#     node = ListNode(i)
#     _node.next = node
#     _node = node
# noderoot = Solution().removeNthFromEnd(noderoot, 2)
# noderoot = ListNode(1)
# noderoot = Solution().removeNthFromEnd(noderoot, 1)
noderoot = ListNode(1)
noderoot.next = ListNode(2)
noderoot = Solution().removeNthFromEnd(noderoot, 2)
print(noderoot)