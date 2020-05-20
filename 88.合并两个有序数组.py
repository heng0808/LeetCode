#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#
from typing import List
# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index = m + n -1
        index1 = m - 1
        index2 = n - 1
        while True:
            if index1 == -1 and index2 == -1:
                break
            elif index1 == -1:
                nums1[index] = nums2[index2]
                index2 = index2 - 1
            elif index2 == -1:
                nums1[index] = nums1[index1]
                index1 = index1 - 1
            else:
                if nums1[index1] > nums2[index2]:
                    nums1[index] = nums1[index1]
                    index1 = index1 - 1
                else:
                    nums1[index] = nums2[index2]
                    index2 = index2 - 1  
            index = index - 1
        return nums1
# @lc code=end

