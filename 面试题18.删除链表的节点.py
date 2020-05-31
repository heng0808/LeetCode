from Tool.ListNode import ListNode
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        pre = None
        node = head
        while node != None:
            if node.val == val:
                if pre == None:
                    head = node.next
                    node.next = None
                else:
                    pre.next = node.next
                    node.next = None
                break
            else:
                pre = node
                node = node.next
        return head