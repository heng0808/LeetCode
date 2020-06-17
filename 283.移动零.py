#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#
from typing import List
# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, 0
        while left < len(nums) and right < len(nums):
            if nums[right] == 0:
                right += 1
                continue

            if nums[left] != 0:
                left += 1
                continue

            if left < right:
                nums[left] = nums[right]
                nums[right] = 0
            else:
                right = left + 1
            
# @lc code=end
nums = [1,1,0,3,12]
Solution().moveZeroes(nums)
print(nums)