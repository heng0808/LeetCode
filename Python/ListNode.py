class ListNode:
    def __init__(self, x):
        self.val = x
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
        head = None
        node = None
        for val in vals:
            if head == None:
                head = ListNode(val)
                node = head
            else:
                node.next = ListNode(val)
                node = node.next
        return head