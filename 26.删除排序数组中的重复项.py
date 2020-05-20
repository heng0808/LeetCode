#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#
from typing import List
# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nextIndex = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[nextIndex - 1]:
                nums[nextIndex] = nums[i]
                nextIndex = nextIndex + 1
        return 0 if len(nums) == 0 else nextIndex
# @lc code=end
print(Solution().removeDuplicates([]))
