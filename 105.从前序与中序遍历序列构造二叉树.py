#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import List
from Tool.Python.TreeNode import TreeNode
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def tree(preorder_l:int, preorder_r:int, inorder_l:int, inorder_r:int) -> TreeNode:
            node = TreeNode(preorder[preorder_l], None, None)
            inorder_root_index = inorder_table[node.val]
            inorder_left_range = [inorder_l, inorder_root_index - 1]
            inorder_right_range = [inorder_root_index + 1, inorder_r]
            if inorder_left_range[-1] - inorder_left_range[0] >= 0:
                # 有左子树
                preorder_left_range = [preorder_l + 1, preorder_r]
                for index in range(preorder_l + 1, preorder_r + 1):
                    if inorder_table[preorder[index]] > inorder_left_range[-1]:
                        preorder_left_range[-1] = index - 1
                        break
                node.left = tree(preorder_left_range[0], preorder_left_range[-1], inorder_left_range[0], inorder_left_range[-1])
                
            if inorder_right_range[-1] - inorder_right_range[0] >= 0:
                # 有右子树
                preorder_right_range = [preorder_l + 1, preorder_r]
                for index in range(preorder_r, preorder_l, -1):
                    if inorder_table[preorder[index]] < inorder_right_range[0]:
                        preorder_right_range[0] = index + 1
                        break
                node.right = tree(preorder_right_range[0], preorder_right_range[-1], inorder_right_range[0], inorder_right_range[-1])
            return node
        inorder_table = {val: i for i, val in enumerate(inorder)}
        root = None
        if len(inorder_table) > 0:
            root = tree(0, len(preorder) - 1, 0, len(inorder) - 1)
        return root
# @lc code=end
# print(Solution().buildTree([3,9,20,15,7], [9,3,15,20,7]))
print(Solution().buildTree([1,2,3], [1,2,3]))