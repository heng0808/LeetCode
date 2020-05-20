#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个有序数组的中位数
#
from typing import List
from math import ceil
# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        count = len(nums1) + len(nums2)
        k = ceil((len(nums1) + len(nums2)) / 2)
        while k > 1:
            k_nums1 = min(k // 2, len(nums1))
            k_nums2 = min(k // 2, len(nums2))
            if len(nums1) == 0:
                nums2 = nums2[k_nums2:] 
                k = k - k_nums2
            elif len(nums2) == 0:
                nums1 = nums1[k_nums1:] 
                k = k - k_nums1
            else:
                if nums1[k_nums1 - 1] < nums2[k_nums2 - 1]:
                    nums1 = nums1[k_nums1:] 
                    k = k - k_nums1
                else:
                    nums2 = nums2[k_nums2:] 
                    k = k - k_nums2
        if count % 2 == 0:
            if len(nums1) == 0:
                return (nums2[0] + nums2[1]) / 2
            elif len(nums2) == 0:
                return (nums1[0] + nums1[1]) / 2            
            else:
                if nums1[0] < nums2[0]:
                    if len(nums1) > 1:
                        return (nums1[0] + min(nums1[1], nums2[0])) / 2            
                    else:
                        return (nums1[0] + nums2[0]) / 2   
                else:
                    if len(nums2) > 1:
                        return (nums2[0] + min(nums2[1], nums1[0])) / 2            
                    else:
                        return (nums1[0] + nums2[0]) / 2           
        else:
            if len(nums1) == 0:
                return nums2[0]
            elif len(nums2) == 0:
                return nums1[0]
            else:
                return min(nums1[0], nums2[0])
# @lc code=end
print(Solution().findMedianSortedArrays([1,3], [2]))
