from __future__ import annotations
from typing import Generic, TypeVar

T = TypeVar("T", str, int)

class TreeNode(Generic[T]):
    # 根据数组构造完全二叉树
    @staticmethod
    def build(vals:List[int]):
        def create_node(index: int) -> TreeNode[T]:
            if index >= len(vals):
                return None
            if vals[index] is None:
                return None
            node = TreeNode(vals[index])
            node.left = create_node(2 * index + 1)
            node.right = create_node(2 * index + 2)
            return node
        return create_node(0)

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    # 前序：中左右
    def font_order(self) -> [T]:
        stack = [self]
        values = []
        while len(stack) != 0:
            node = stack.pop()
            values.append(node.val)
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)
        return values

    # 中序：左中右
    def middle_order(self) -> [T]:
        head = self
        stack = []
        values = []
        while head is not None or len(stack) != 0:
            if head is not None:
                stack.append(head)
                head = head.left
            else:
                head = stack.pop()
                values.append(head.val)
                head = head.right
        return values

    # 后序：左右中=~中右左
    def back_order(self) -> [T]:
        stack = [self]
        values = []
        while len(stack) != 0:
            node = stack.pop()
            values.append(node.val)
            if node.left is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)
        return values[::-1]

    def level_order_array(self) -> []:
        queue = [self]
        values = []
        while len(queue) != 0:
            node = queue[0]
            values.append(node.val)
            del queue[0]
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        return values