class ListNode:
    def __init__(self, vals:[int]):
        if len(vals) == 0:
            raise ValueError('vals is invalid')
        self.val = vals[0]
        try:
            self.next = ListNode(vals[1:])
        except:
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