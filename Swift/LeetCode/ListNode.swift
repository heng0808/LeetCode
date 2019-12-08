//
//  ListNode.swift
//  LeetCode
//
//  Created by zhangheng on 2019/12/8.
//  Copyright © 2019 zhangheng. All rights reserved.
//

import Cocoa

public class ListNode:CustomStringConvertible {
    public var val: Int
    public var next: ListNode?
    public init(_ val: Int) {
        self.val = val
        self.next = nil
    }
    
    public var description: String {
        var values:[Int] = []
        var node:ListNode? = self
        while node != nil {
            values.append(node!.val)
            node = node?.next
        }
        return values.description
    }
    
    static func Node(_ values:[Int]) -> ListNode? {
        if values.isEmpty {
            return nil
        }
        let node = ListNode(values.first!)
        var temp:ListNode = node
        for value in values[1..<values.count] {
            temp.next = ListNode(value)
            temp = temp.next!
        }
        return node
    }
}
