#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#
from Tool.Python.TreeNode import TreeNode
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        nodes = [] if not root else [root]
        while len(nodes) > 0:
            leaf_nodes = []
            for node in nodes:
                leaf_nodes.append(node.left if node and node.left else None)
                leaf_nodes.append(node.right if node and node.right else None)
            left, right, ok_nodes_count  = 0, len(leaf_nodes) - 1, 0
            while left < right:
                if leaf_nodes[left]:
                    ok_nodes_count += 1
                if leaf_nodes[right] :
                    ok_nodes_count += 1
                if leaf_nodes[left] and leaf_nodes[right] and leaf_nodes[left].val == leaf_nodes[right].val:
                    left += 1
                    right -= 1
                    continue
                if not leaf_nodes[left] and not leaf_nodes[right]:
                    left += 1
                    right -= 1
                    continue
                return False
            if ok_nodes_count > 0:
                nodes = leaf_nodes
            else:
                nodes = []
        return True

# @lc code=end
print(Solution().isSymmetric(TreeNode([1,2,2,None,3,None,3])))