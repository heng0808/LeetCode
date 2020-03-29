# 给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。
# 
# 示例 1:
# 输入: 1->2->3->4->5->NULL, k = 2
# 输出: 4->5->1->2->3->NULL
# 解释:
# 向右旋转 1 步: 5->1->2->3->4->NULL
# 向右旋转 2 步: 4->5->1->2->3->NULL
# 
# 示例 2:
# 输入: 0->1->2->NULL, k = 4
# 输出: 2->0->1->NULL
# 解释:
# 向右旋转 1 步: 2->0->1->NULL
# 向右旋转 2 步: 1->2->0->NULL
# 向右旋转 3 步: 0->1->2->NULL
# 向右旋转 4 步: 2->0->1->NULL

from Tool.ListNode import ListNode

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head == None:
            return head

        prevewNode = head
        count = 1
        while prevewNode.next != None:
            prevewNode = prevewNode.next
            count = count + 1
        prevewNode.next = head

        node = head
        retainCount = count - k % count
        while retainCount > 0:
            prevewNode = node
            node = node.next
            retainCount = retainCount - 1
        head = node
        prevewNode.next = None
        return head

print(Solution().rotateRight(ListNode([1,2,3,4,5]), 1))
print(Solution().rotateRight(ListNode([0,1,2]), 3))
print(Solution().rotateRight(ListNode([1,2]), 2))
# print(Solution().rotateRight(None, 0))