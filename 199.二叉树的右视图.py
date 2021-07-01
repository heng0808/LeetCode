#
# @lc app=leetcode.cn id=199 lang=python3
#
# [199] 二叉树的右视图
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
    def rightSideView(self, root: TreeNode) -> List[int]:
        ans = []
        levelNode = [root] if root else []
        while len(levelNode) > 0:
            rightVal = None
            _levelNode = []
            for node in levelNode:
                rightVal = node.val
                if node.left:
                    _levelNode.append(node.left)
                if node.right:
                    _levelNode.append(node.right)
            ans.append(rightVal)
            levelNode = _levelNode
        return ans
# @lc code=end
tree = TreeNode.build([1,2])
print(Solution().rightSideView(tree))