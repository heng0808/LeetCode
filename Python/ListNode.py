class ListNode:
    def __init__(self, vals: []):
            self.val = vals[0]
            if len(vals) > 1:
                self.next = ListNode(vals[1:])
            else:
                self.next = None

    def __str__(self):
        if self.next == None:
            return str(self.val)
        des = str(self.val)
        node = self.next
        while node:
            des = des + " -> " + str(node.val)
            node = node.next
        return des

    @staticmethod
    def node(vals: []):
        if len(vals) > 0:
            return ListNode(vals)
        return None