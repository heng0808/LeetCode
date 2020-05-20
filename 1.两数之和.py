#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#
from typing import List
# @lc code=start
class Solution:
    def twoSum(self, nums, target) -> List[int]:
        num_map = {}
        for index in range(0, len(nums)):
            num = nums[index]
            res = target - num
            if res in num_map:
                return [index, num_map[res]]
            num_map[num] = index
        return []
# @lc code=end

