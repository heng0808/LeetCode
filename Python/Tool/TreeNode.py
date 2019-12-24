from __future__ import annotations

class TreeNode:
    def __init__(self, val:int, left:TreeNode, right:TreeNode):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def node(vals: []):
        # 完全二叉树通过当前节点可以知道子节点的位置
        def createNode(index:int) -> TreeNode:
            if index >= len(vals):
                return None
            if vals[index] == None:
                return None
            return TreeNode(val=vals[index], left=createNode(2 * index + 1), right=createNode(2 * index + 2))
        return createNode(0)