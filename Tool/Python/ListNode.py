from typing import List

class ListNode:
    @staticmethod
    def build(vals:List):
        if len(vals) == 0:
            return None
        return ListNode(val=vals[0], next=ListNode.build(vals[1:]))
        
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        if self.next == None:
            return str(self.val)
        des = str(self.val)
        node = self.next
        while node:
            des = des + " -> " + str(node.val)
            node = node.next
        return des