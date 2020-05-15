#
# @lc app=leetcode.cn id=560 lang=python3
#
# [560] 和为K的子数组
#
from typing import List
# @lc code=start
class Solution:
    # 前缀和 + 哈希表优化
    # sum[i,j] = sum[0,j] - sum[0,i]
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        pre_sum = 0
        pre_map = {0:1}
        for i in range(0, len(nums)):
            pre_sum = pre_sum + nums[i]
            ans = ans + pre_map.get(pre_sum - k, 0)
            pre_map[pre_sum] = pre_map.get(pre_sum, 0) + 1
        return ans
    # 枚举
    # def subarraySum(self, nums: List[int], k: int) -> int:
    #     ans = 0
    #     for i in range(0, len(nums)):
    #         sum = 0
    #         for j in range(i, len(nums)):
    #             sum = sum + nums[j]
    #             if sum == k:
    #                 ans = ans + 1
    #         pass
    #     return ans
# @lc code=end
print(Solution().subarraySum([1,2,3], 3))
