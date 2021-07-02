#
# @lc app=leetcode.cn id=138 lang=python3
#
# [138] 复制带随机指针的链表
#

# @lc code=start

# Definition for a Node.
class Node:
    def __init__(self, x: int, next = None, random = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: Node) -> Node:
        # return self.function1(head)
        return self.function2(head)
    
    # 拼接+拆分
    # node1->node1_copy->node2->node2_copy ...
    def function2(self, head) -> Node:
        if head == None:
            return head

        # 拼接
        node = head
        while node:
            node_copy = Node(node.val)
            node_next = node.next
            node.next = node_copy
            node_copy.next = node_next
            node = node_next
        
        # 链接random
        node = head
        while node:
            if node.random:
                node_copy = node.next
                node_copy.random = node.random.next
            node = node.next.next

        # 拆分
        head_copy = head.next
        node_copy = head_copy
        while node_copy:
            if node_copy.next:
                node_copy.next = node_copy.next.next
                node_copy = node_copy.next
            else:
                break

        return head_copy

    # 哈希表
    # node : node_copy
    def function1(self, head) -> Node:
        if head == None:
            return None

        node_copy_map = dict()
        node_copy_arr = []

        node = head
        while node:
            node_copy = Node(node.val)
            if len(node_copy_arr) > 0:
                node_copy_arr[-1].next = node_copy
            node_copy_arr.append(node_copy)
            node_copy_map[node] = node_copy
            node = node.next

        node = head
        node_copy = node_copy_arr[0]
        while node and node_copy:
            if node.random:
                node_copy_map[node].random = node_copy_map[node.random]
            node = node.next
            node_copy = node_copy.next

        return node_copy_arr[0]
        
# @lc code=end
node4 = Node(1)
node3 = Node(10, node4)
node2 = Node(11, node3)
node1 = Node(13, node2)
node0 = Node(7, node1)

node1.random = node0
node2.random = node4
node3.random = node2
node4.random = node0

# [[7,null],[13,0],[11,4],[10,2],[1,0]]
node = Solution().copyRandomList(node0)