#
# @lc app=leetcode.cn id=674 lang=python3
#
# [674] 最长连续递增序列
#
from typing import List
# @lc code=start
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        stack = []
        index = 0
        ans = 0
        while index < len(nums):
            if len(stack) == 0:
                stack.append(nums[index])
            else:
                if stack[-1] >= nums[index]:
                    ans = max(ans, len(stack))
                    stack.clear()
                stack.append(nums[index])
            index = index + 1
        return max(ans, len(stack))
# @lc code=end
print(Solution().findLengthOfLCIS([1,3,5,4,7]))

