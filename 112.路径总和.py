#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
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
    # 递归
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        sum -= root.val
        if not root.left and not root.right and sum == 0:
            return True
        return self.hasPathSum(root.left, sum) or self.hasPathSum
                
                
# @lc code=end

# root = TreeNode([5,4,8,11,None,13,4,7,2,None,None,None,1])
# root = TreeNode([1,2,None,3,None,4,None,5])
root = TreeNode([1])
print(Solution().hasPathSum(root, 1))

#         5
#      4     8
#   11     13  4
# 7   2          1   