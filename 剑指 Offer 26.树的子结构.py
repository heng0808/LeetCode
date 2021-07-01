from Tool.Python.TreeNode import TreeNode
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        return self.function1(A, B, B)
    def function1(self, A:TreeNode, B:TreeNode, B_head:TreeNode):
        if A == None and B != None:
            return False
        if A != None and B == None:
            return False
        if A == None and B == None:
            return True
        if A.val == B.val:
            # 节点相同
            # 比较左子树和右边子树
            if B.left == None:
                l_res = True
            else:
                if A.left == None:
                    return False
                else:
                    l_res = self.function1(A.left, B.left, B_head)
                
            if B.right == None:
                r_res = True
            else:
                if A.right == None:
                    return False
                else:
                    r_res = self.function1(A.right, B.right, B_head)

            if l_res and r_res:
                return True
            else:
                if B == B_head:
                    if self.function1(A.left, B, B_head):
                        return True
                    if self.function1(A.right, B, B_head):
                        return True
                return False
        else:
            if B == B_head:
                if self.function1(A.left, B, B_head):
                    return True
                if self.function1(A.right, B, B_head):
                    return True
            return False

# nodeA = TreeNode.build([3,4,5,1,2])
# nodeB = TreeNode.build([4,1])
# print(Solution().isSubStructure(nodeA, nodeB))

# nodeA = TreeNode.build([1,2,3,None,5,6,7,8,9,10,11,12,13])
# nodeB = TreeNode.build([3,6,None,None,13])
# print(Solution().isSubStructure(nodeA, nodeB))

# nodeA = TreeNode.build([4,2,3,4,5,6,7,8,9])
# nodeB = TreeNode.build([4,8,9])
# print(Solution().isSubStructure(nodeA, nodeB))

nodeA = TreeNode.build([1,0,1,-4,-3])
nodeB = TreeNode.build([1,-4])
print(Solution().isSubStructure(nodeA, nodeB))


