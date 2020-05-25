#
# @lc app=leetcode.cn id=154 lang=python3
#
# [154] 寻找旋转排序数组中的最小值 II
#
from typing import List
# @lc code=start
class Solution:
    # 二分查找
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                right = mid
        return nums[left]
    # def findMin(self, nums: List[int]) -> int:
    #     i = 1
    #     while i <= len(nums):
    #         if i == len(nums):
    #             i = 0
    #             break
    #         elif nums[i] < nums[i - 1]:
    #             break
    #         i = i + 1
    #     return nums[i] if len(nums) > 0 else 0
# @lc code=end
# print(Solution().findMin([1,3,5]))
print(Solution().findMin([2,2,2,0,1]))