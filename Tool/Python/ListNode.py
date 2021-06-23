from typing import List

class ListNode:
    @staticmethod
    def build(vals:List[int]):
        if len(vals) == 0:
            return None
        return ListNode(val=vals[0], next=ListNode.build(vals[1:]))
        
    def __init__(self, val:int=0, next=None):
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

    def __eq__(self, x) -> bool:
        # ==
        if x == None:
            return False
        return self.val == x.val

    def __ne__(self, x) -> bool:
        # !=
        return self.val != x.val

    def __lt__(self, x) -> bool:
        # <
        return self.val < x.val

    def __gt__(self, x) -> bool:
        # >
        return self.val > x.val

    def __ge__(self, x) -> bool:
        # >=
        return self.val >= x.val

    def __le__(self, x) -> bool:
        # <=
        return self.val <= x.val
