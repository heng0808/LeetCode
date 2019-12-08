//
//  Code4.swift
//  LeetCode
//
//  Created by zhangheng on 2019/12/9.
//  Copyright © 2019 zhangheng. All rights reserved.
//

import Cocoa

class Code4: NSObject {
    func findMedianSortedArrays(_ nums1: [Int], _ nums2: [Int]) -> Double {
        var nums1Stack:[Int] = nums1.reversed()
        var nums2Stack:[Int] = nums2.reversed()
        var numsArr:[Int] = []
        while !nums1Stack.isEmpty || !nums2Stack.isEmpty {
            if numsArr.isEmpty {
                if nums1Stack.isEmpty {
                    numsArr.append(nums2Stack.popLast()!)
                } else if nums2Stack.isEmpty {
                    numsArr.append(nums1Stack.popLast()!)
                } else if (nums1Stack.last! < nums2Stack.last!) {
                    numsArr.append(nums1Stack.popLast()!)
                } else {
                    numsArr.append(nums2Stack.popLast()!)
                }
                continue
            }
            if nums1Stack.last ?? 999999999 < nums2Stack.last ?? 999999999 {
                numsArr.append(nums1Stack.popLast()!)
            } else {
                numsArr.append(nums2Stack.popLast()!)
            }
        }
        if numsArr.count % 2 == 0 {
            return Double(numsArr[numsArr.count / 2] + numsArr[(numsArr.count / 2) - 1]) / 2
        } else {
            return Double(numsArr[numsArr.count / 2])
        }
    }
}
