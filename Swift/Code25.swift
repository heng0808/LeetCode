//
//  Code25.swift
//  LeetCode
//
//  Created by zhangheng on 2019/12/9.
//  Copyright © 2019 zhangheng. All rights reserved.
//

import Cocoa

// not done
class Code25: NSObject {
    func reverseKGroup(_ head: ListNode?, _ k: Int) -> ListNode? {
        // 栈
        var reverseNode:ListNode?
        var reverseNodeLast:ListNode?
        var root:ListNode? = head
        var stack:[ListNode] = []
        while root != nil && k > 1 {
            stack.append(root!)
            root = root?.next
            if stack.count == k {
                while !stack.isEmpty {
                    if reverseNode == nil {
                        reverseNode = stack.popLast()
                        reverseNodeLast = reverseNode
                    } else {
                        reverseNodeLast?.next = stack.popLast()
                        reverseNodeLast = reverseNodeLast?.next
                    }
                }
            }
        }
        stack.forEach { (node) in
            reverseNodeLast?.next = node
            reverseNodeLast = reverseNodeLast?.next
        }
        reverseNodeLast?.next = nil
        return reverseNode ?? head
//        // 指针
//        var begin:ListNode?
//        var root:ListNode? = head
//        var temp:ListNode? = head
//        var rootLast:ListNode? = nil
//        var count = 1
//        while temp != nil && k > 1 {
//            if count == k {
//                let rootCurrent:ListNode? = root
//                let tempNext:ListNode? = temp?.next
//                if begin == nil {
//                    begin = temp
//                }
//                while root !== temp {
//                    let rootNext:ListNode? = root?.next
//                    root?.next = temp?.next
//                    temp?.next = root
//                    root = rootNext
//                }
//                if rootLast != nil {
//                    rootLast?.next = temp
//                }
//                rootLast = rootCurrent
//                temp = tempNext
//                root = temp
//                count = 1
//            } else {
//                temp = temp?.next
//                count += 1
//            }
//        }
//        return begin ?? head
    }
}
