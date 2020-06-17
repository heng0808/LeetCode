#
# @lc app=leetcode.cn id=226 lang=python3
#
# [226] 翻转二叉树
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
    def invertTree(self, root: TreeNode) -> TreeNode:
        nodes_queue = [root] if root else []
        while len(nodes_queue) > 0:
            node = nodes_queue.pop(0)
            temp = node.left
            node.left = node.right
            node.right = temp
            if node.left:
                nodes_queue.append(node.left)
            if node.right:
                nodes_queue.append(node.right)
        return root
# @lc code=end

