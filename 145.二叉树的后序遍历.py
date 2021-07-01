#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
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
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        # 左右中=reverse(中右左)
        ans = []
        stack = [] if not root else [root]
        node = root
        while len(stack) > 0:
            node = stack.pop()
            ans.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        ans.reverse()
        return ans

    # 其他做法
    # def postorderTraversal(self, root: TreeNode) -> List[int]:
    #     ans = []
    #     stack = []
    #     node = root
    #     while len(stack) > 0 or node != None:
    #         if node != None:
    #             ans.append(node.val)
    #             stack.append(node)
    #             node = node.right
    #         else:
    #             node = stack.pop()
    #             node = node.left
    #     ans.reverse()
    #     return ans

# @lc code=end
print(Solution().postorderTraversal(TreeNode.build([1,None,2,None,None,3])))

