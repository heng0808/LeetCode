#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
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
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # 左中右
        # 默认当左，有左就扔，没左就弹，弹了看右
        ans = []
        stack = []
        node = root
        while len(stack) > 0 or node != None:
            if node != None:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                ans.append(node.val)
                node = node.right
        return ans
        
# @lc code=end
print(Solution().inorderTraversal(TreeNode.build([1,None,2,None,None,3])))
