#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#
from typing import List
# total(i) = max(num[i] + total[i-2], total[i-1])
# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        total = [0] * len(nums)
        total[0] = nums[0]
        total[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            total[i] = max(nums[i] + total[i-2], total[i-1])
        return total[-1]
# @lc code=end
print(Solution().rob([2,1,1,2]))
