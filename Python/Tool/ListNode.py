class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def buildNode(vals:str):
    if len(vals) == 0:
        return None
    rootNode: ListNode = None
    node:ListNode = None
    for val in vals:
        if rootNode == None:
            rootNode = ListNode(int(val))
            node = rootNode
            continue
        else:
            node.next = ListNode(int(val))
            node = node.next

    return rootNode

