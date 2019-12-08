//
//  TreeNode.swift
//  LeetCode
//
//  Created by zhangheng on 2019/12/8.
//  Copyright © 2019 zhangheng. All rights reserved.
//

import Cocoa

public class TreeNode {
    public var val: Int
    public var left: TreeNode?
    public var right: TreeNode?
    public init(_ val: Int) {
        self.val = val
        self.left = nil
        self.right = nil
    }
//    // 满二叉树 除了最后一层 其他层都有两个子节点
//    // 当二叉树的深度为h时，它的h层节点必须都是连续靠左并不可隔开的(满二叉树也符合)，并且1～h-1层的结点数都达到最大个数(即1~h-1层为一个满二叉树)。
//    static func buildNode(_ values:[Int]?) -> TreeNode?{
//        if values == nil || values!.isEmpty {
//            return nil
//        }
//        let node = TreeNode((values?.first)!)
//        node.left =
//        return nil
//    }
}
