from Tool.Python.TreeNode import TreeNode
import sys

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        ans = 0
        def depthNode(node:TreeNode) -> int:
            if node == None:
                return 0
            nonlocal ans
            l = depthNode(node.left)
            r = depthNode(node.right)
            ans = max(ans, l + r + 1)
            return max(l, r) + 1
        depthNode(root)
        return ans - 1 if ans >1 else 0

tree = TreeNode[int].node([1,2,3,4,5])
print(Solution().diameterOfBinaryTree(tree))