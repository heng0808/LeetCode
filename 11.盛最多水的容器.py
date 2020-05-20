#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#
from typing import List
# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        left = 0
        right = len(height) - 1
        while left < right:
            ans = max(ans, (right - left) * min(height[right], height[left]))
            if height[left] < height[right]:
                left = left + 1
            else:
                right = right - 1
        return ans
    # Time Limit
    # def maxArea(self, height: List[int]) -> int:
    #     water = 1
    #     ans = 0
    #     while True:
    #         left = 0
    #         right = len(height) - 1
    #         while left < right:
    #             if height[left] < water:
    #                 left = left + 1
    #                 continue
    #             elif height[right] < water:
    #                 right = right - 1
    #                 continue
    #             else:
    #                 ans = max(ans, (right - left) * water)
    #                 break
    #         if left == right:
    #             break
    #         else:
    #             water = water + 1
    #     return ans
# @lc code=end
print(Solution().maxArea([2,3,4,5,18,17,6]))
