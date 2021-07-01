#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层次遍历
#
from typing import List
from Tool.Python.TreeNode import TreeNode
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        nodes, level = [root] if root else [], 0
        ans = []
        while len(nodes) > 0:
            _nodes = []
            ans.append([])
            if level % 2 == 0:
                for node in nodes:
                    ans[-1].append(node.val)
                
            else:
                for node in reversed(nodes):
                    ans[-1].append(node.val)
            for node in nodes:
                if node.left:
                    _nodes.append(node.left)
                if node.right:
                    _nodes.append(node.right)
            nodes = _nodes
            level += 1
        return ans
# @lc code=end
tree = TreeNode.build([3,9,20,None,None,15,7])
print(Solution().zigzagLevelOrder(tree))

