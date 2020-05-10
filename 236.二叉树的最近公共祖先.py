#
# @lc app=leetcode.cn id=236 lang=python3
#
# [236] 二叉树的最近公共祖先
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
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        p_stack = []
        q_stack = []
        def findNode(root:TreeNode, _node:TreeNode, stack:[TreeNode]) -> []:
            if root == _node:
                stack.append(root)
                return stack
            else:
                stack.append(root)
                if root.left != None:
                    if findNode(root.left, _node, stack):
                        return stack
                if root.right != None:
                    if findNode(root.right, _node, stack):
                        return stack
                stack.pop()
        p_stack = findNode(root, p, [])
        q_stack = findNode(root, q, [])
        index = 0
        while True:
            if index >= len(p_stack):
                return p_stack[index - 1]
            elif index >= len(q_stack):
                return q_stack[index - 1]
            elif p_stack[index] == q_stack[index]:
                index = index + 1
            else:
                return p_stack[index - 1]
# @lc code=end
root = TreeNode.node([3,5,1,6,2,0,8,None,None,7,4])
p = root.left
q = root.left.right.right
print(Solution().lowestCommonAncestor(root, p, q).val)