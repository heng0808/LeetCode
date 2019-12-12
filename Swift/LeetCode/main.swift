//
//  main.swift
//  LeetCode
//
//  Created by zhangheng on 2019/12/8.
//  Copyright © 2019 zhangheng. All rights reserved.
//

import Foundation

// Code94
//let root = TreeNode(1)
//root.right = TreeNode(2)
//root.right?.left = TreeNode(3)
//print(Code94().inorderTraversal(root))
// Code144
//print(Code144().preorderTraversal(root))
// Code145
//print(Code145().postorderTraversal(root))
// Code104
//print(Code104().maxDepth(root))
// Code2
//let node1:ListNode = ListNode.Node([2,4,3])!
//let node2:ListNode = ListNode.Node([5,6,4])!
//print(Code2().addTwoNumbers(node1, node2) ?? "none")
// Code4
//print(Code4().findMedianSortedArrays([3], [-2,-1]))
// Code25
//print(Code25().reverseKGroup(ListNode.Node([1,2]), 2)!)
// Code26
//var arr:[Int] = [0,0,1,1,1,2,2,3,3,4]
var arr:[Int] = [1]
print(Code26().removeDuplicates(&arr))
print(arr)
