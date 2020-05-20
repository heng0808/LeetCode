#
# @lc app=leetcode.cn id=217 lang=python3
#
# [217] 存在重复元素
#
from typing import List
# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        table = {}
        for num in nums:
            if num in table:
                return True
            else:
                table[num] = 1
        return False
# @lc code=end

