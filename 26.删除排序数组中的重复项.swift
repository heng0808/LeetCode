//
//  Code26.swift
//  LeetCode
//
//  Created by zhang heng on 2019/12/11.
//  Copyright © 2019 zhangheng. All rights reserved.
//

import Cocoa

class Code26 {
    func removeDuplicates(_ nums: inout [Int]) -> Int {
        if nums.count == 0 {
            return 0
        }
        nums.append(nums.remove(at: 0))
        var left = 0
        let right = nums.count - 1
        var begin = right
        while left < right {
            if nums[left] > nums.last! {
                nums.append(nums.remove(at: left))
                begin -= 1
            } else {
                left += 1
            }
        }
        let count = nums.count - begin
        while begin > 0 {
            nums.append(nums.remove(at: 0))
            begin -= 1
        }
        return count
    }
}
