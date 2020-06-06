from typing import List
from Tool.Python.TreeNode import TreeNode

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


