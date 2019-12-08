//
//  Code104.swift
//  LeetCode
//
//  Created by zhangheng on 2019/12/8.
//  Copyright © 2019 zhangheng. All rights reserved.
//

import Cocoa

class Code104: NSObject {
    func maxDepth(_ root: TreeNode?) -> Int {
        if root == nil {
            return 0
        }
        var maxDepth = 0
        var stack:[TreeNode] = [root!]
        while stack.isEmpty == false {
            if stack.last?.left != nil {
                // 有左子树
                stack.append(stack.last!.left!)
            } else if (stack.last?.right != nil) {
                // 有右子属
                stack.append(stack.last!.right!)
            } else {
                // 什么都没有
                maxDepth = max(maxDepth, stack.count)
                let node = stack.popLast()
                if stack.last?.left === node {
                    stack.last?.left = nil
                } else if stack.last?.right === node{
                    stack.last?.right = nil
                }
            }
        }
        return maxDepth
    }
}
