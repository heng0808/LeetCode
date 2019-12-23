from __future__ import annotations

class TreeNode:
    def __init__(self, val:int, left:TreeNode, right:TreeNode):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def node(vals: []):
        # 完全二叉树通过当前节点可以知道子节点的位置
        stack = []
        for val in vals:
            if len(stack) == 0:

        if len(vals) > 0:
            return ListNode(vals)
        return None