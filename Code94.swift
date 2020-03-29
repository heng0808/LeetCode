//
//  Code94.swift
//  LeetCode
//
//  Created by zhangheng on 2019/12/8.
//  Copyright © 2019 zhangheng. All rights reserved.
//

import Cocoa

class Code94 {
//  中序：左中右
    func inorderTraversal(_ root: TreeNode?) -> [Int] {
        if root == nil {
            return []
        }
//        // 递归
//        return inorderTraversal(root?.left) +[root!.val] +inorderTraversal(root!.right)
        // 非递归  bbbbbbbbbbbb
        var stack:[TreeNode] = []
        var head:TreeNode? = root!
        var values:[Int] = []
        while !stack.isEmpty || head != nil{
            if head != nil {
                stack.append(head!)
                head = head?.left
            } else {
                head = stack.popLast()
                values.append(head!.val)
                head = head?.right
            }
        }
        return values
    }
}
