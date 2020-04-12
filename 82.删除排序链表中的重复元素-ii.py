#
# @lc app=leetcode.cn id=82 lang=python3
#
# [82] 删除排序链表中的重复元素 II
#
from Python.ListNode import ListNode
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        _head = None
        _headNode = None
        node, isDuplicate = head, False
        while node != None and  node.next != None:
            if node.val != node.next.val:
                if isDuplicate == False:
                    if _headNode == None:
                        _head = ListNode(node.val)
                        _headNode = _head
                    else:
                        _headNode.next = ListNode(node.val)
                        _headNode = _headNode.next
                node, isDuplicate = node.next, False
            else:
                node, isDuplicate = node.next, True
        if isDuplicate == False:
            if _head == None:
                _head = node
            if _headNode == None:
                _headNode = node
            else:
                _headNode.next = node
                _headNode = _headNode.next
            pass
        return _head
# @lc code=end
print(Solution().deleteDuplicates(None))
print(Solution().deleteDuplicates(ListNode.node([1,2,2])))
print(Solution().deleteDuplicates(ListNode.node("1->2->3->3->4->4->5".split("->"))))
print(Solution().deleteDuplicates(ListNode.node("1->1->1->2->3".split("->"))))
