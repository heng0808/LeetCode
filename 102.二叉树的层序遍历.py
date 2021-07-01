#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
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
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        arr = []
        nextLevelNodes = []
        if root != None:
            nextLevelNodes = [root]
        while len(nextLevelNodes) > 0:
            levelVals = []
            _nextLevelNodes = []
            for node in nextLevelNodes:
                levelVals.append(node.val)
                if node.left:
                    _nextLevelNodes.append(node.left)
                if node.right:
                    _nextLevelNodes.append(node.right)
            arr.append(levelVals)
            nextLevelNodes = _nextLevelNodes
        return arr
# @lc code=end
root = TreeNode.build([3,9,20,None,None,15,7])
print(Solution().levelOrder(root))

