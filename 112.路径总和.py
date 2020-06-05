#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
#
from Tool.TreeNode import TreeNode
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 递归
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        def nextStep(length:int, node:TreeNode) -> bool:
            if node == None:
                return False
            else:
                length = length + node.val
                if node.left == None and node.right == None:
                    if length == sum:
                        return True
                if node.left != None:
                    if nextStep(length, node.left):
                        return True
                if node.right != None:
                    if nextStep(length, node.right):
                        return True
                return False
        return nextStep(0, root)
                
# @lc code=end

# root = TreeNode.node(values=[5,4,8,11,None,13,4,7,2,None,None,None,1])
# root = TreeNode.node(values=[1,2,None,3,None,4,None,5])
root = TreeNode.node(values=[1])
print(Solution().hasPathSum(root, 1))

#         5
#      4     8
#   11     13  4
# 7   2          1   