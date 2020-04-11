#
# @lc app=leetcode.cn id=80 lang=python3
#
# [80] 删除排序数组中的重复项 II
#
from typing import List
# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        moveDistance = 0
        findIndex = 0
        while findIndex < len(nums):
            if findIndex > 1:
                if nums[findIndex] != nums[findIndex - 2 - moveDistance]:
                    nums[findIndex - moveDistance] = nums[findIndex]
                else:
                    moveDistance = moveDistance + 1
            findIndex = findIndex + 1
        return len(nums) - moveDistance
# @lc code=end

# nums = [1,1,1,2,2,3]
# nums = [1,1,1,2,2,2,3,3,3,4,4,4]
nums = []
print(nums[0:Solution().removeDuplicates(nums)])