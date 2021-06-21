from Tool.Python.ListNode import ListNode

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        leftNode, rightNode = head, head
        while k > 1:
            if rightNode.next == None:
                return None
            else:
                k -= 1
                rightNode = rightNode.next
        while rightNode.next:
            leftNode = leftNode.next
            rightNode = rightNode.next
        return leftNode

print(Solution().getKthFromEnd(ListNode.build([1]), 1))
