# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from Tool.Python.ListNode import ListNode
from typing import List
class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        arr = []
        while head != None:
            arr.append(head.val)
            head = head.next
        l, r = 0, len(arr) - 1
        while l < r:
            val = arr[l]
            arr[l] = arr[r]
            arr[r] = val
            l = l + 1
            r = r - 1
        return arr
