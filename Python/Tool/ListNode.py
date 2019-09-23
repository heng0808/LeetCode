class ListNode:
    def __init__(self, vals: []):
        if len(vals) > 0:
            self.val = vals[0]
            if len(vals) > 1:
                self.next = ListNode(vals[1:])
            else:
                self.next = None
