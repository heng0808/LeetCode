from Tool.Python.ListNode import ListNode
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        node = head
        while node != None:
            nodeNext = node.next
            if pre == None:
                pre = node
                node = nodeNext
                pre.next = None
            else:
                node.next = pre
                pre = node
                node = nodeNext
        return pre

print(Solution().reverseList(ListNode([1,2,3,4,5])))