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
        var begin:ListNode?
        var root:ListNode? = head
        var temp:ListNode? = ListNode(0)
        temp?.next = root
        var count = 1
        while temp != nil {
            if count == k {
                let next:ListNode? = temp?.next
                if begin == nil {
                    begin = next
                }
                while !(root?.next === temp) {
                    let rootNext = root?.next
                    let tempNext = temp?.next?.next
                    root?.next = tempNext
                    root = rootNext
                }
                count = 1
                root = next
                temp = next
            } else {
                count += 1
                temp = temp?.next
            }
        }
        return begin
    }
}
