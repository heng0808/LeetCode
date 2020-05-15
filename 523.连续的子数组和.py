#
# @lc app=leetcode.cn id=523 lang=python3
#
# [523] 连续的子数组和
#
from typing import List
# @lc code=start
class Solution:
    # 枚举
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        for i in range(0, len(nums)):
            sum = 0
            for j in range(i, len(nums)):
                sum = sum + nums[j]
                if j - i > 0:
                    if k == 0 and sum == 0:
                        return True
                    elif k != 0 and sum % k == 0:
                        return True                    
        return False
# @lc code=end
print(Solution().checkSubarraySum([23,2,6,4,7], -6))
