#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] 路径总和 II
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
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        ans = []
        def nextNode(path:[int], node:TreeNode, pre_sum:int):
            if len(path) == 0 and node == None:
                return
            cur_sum = pre_sum + node.val
            cur_path = path + [node.val]
            if not node.left and not node.right and cur_sum == sum:
                ans.append(cur_path)
            else:
                if node.left:
                    nextNode(cur_path, node.left, cur_sum)
                if node.right:
                    nextNode(cur_path, node.right, cur_sum)
        nextNode([], root, 0)
        return ans
# @lc code=end
root = TreeNode([5,4,8,11,None,13,4,7,2,None,None,None,None,5,1])
print(Solution().pathSum(root, 22))

