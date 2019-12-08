//
//  Code145.swift
//  LeetCode
//
//  Created by zhangheng on 2019/12/8.
//  Copyright © 2019 zhangheng. All rights reserved.
//

import Cocoa

class Code145: NSObject {
//  后序：左右中
    func postorderTraversal(_ root: TreeNode?) -> [Int] {
        if root == nil {
            return []
        }
//        // 递归
//        return postorderTraversal(root?.left) + postorderTraversal(root!.right) + [root!.val]
        // 非递归
        var stack:[TreeNode] = []
        var values:[Int] = []
        var head:TreeNode? = root
        while stack.isEmpty == false || head != nil {
            if (head != nil) {
                values.append(head!.val)
                stack.append(head!)
                head = head?.right
            } else {
                head = stack.popLast()
                head = head?.left
            }
        }
        return values.reversed()
    }
}
