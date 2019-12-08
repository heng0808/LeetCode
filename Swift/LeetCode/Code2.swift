//
//  Code2.swift
//  LeetCode
//
//  Created by zhangheng on 2019/12/8.
//  Copyright © 2019 zhangheng. All rights reserved.
//

import Cocoa

class Code2: NSObject {
    func addTwoNumbers(_ l1: ListNode?, _ l2: ListNode?) -> ListNode? {
        if l1 == nil || l2 == nil {
            return nil
        }
        var node1:ListNode? = l1
        var node2:ListNode? = l2
        var tempNode:ListNode = ListNode(0)
        let sumNode:ListNode = tempNode
        while node1 != nil || node2 != nil {
            tempNode.val += node1?.val ?? 0
            node1 = node1?.next

            tempNode.val += node2?.val ?? 0
            node2 = node2?.next
            
            if tempNode.val > 9 {
                tempNode.next = ListNode(tempNode.val / 10)
                tempNode.val = tempNode.val % 10
            } else if (node1 != nil || node2 != nil) {
                tempNode.next = ListNode(0)
            }
            if tempNode.next != nil {
                tempNode = tempNode.next!
            }
        }
        return sumNode
    }
}
