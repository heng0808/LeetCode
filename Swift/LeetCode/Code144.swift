//
//  Code144.swift
//  LeetCode
//
//  Created by zhangheng on 2019/12/8.
//  Copyright © 2019 zhangheng. All rights reserved.
//

import Cocoa

class Code144: NSObject {
//  深度优先搜索就是树的先序遍历
//  前序：中左右
    func preorderTraversal(_ root: TreeNode?) -> [Int] {
        if root == nil {
            return []
        }
//        // 递归
//        return [root!.val] + preorderTraversal(root?.left) + preorderTraversal(root!.right)
        // 非递归
        var stack:[TreeNode] = []
        var head:TreeNode = root!
        var values:[Int] = []
        stack.append(head)
        while stack.isEmpty == false {
            head = stack.popLast()!
            values.append(head.val)
            if head.right != nil {
                stack.append(head.right!)
            }
            if head.left != nil {
                stack.append(head.left!)
            }
        }
        return values
    }
}
