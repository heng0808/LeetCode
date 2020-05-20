#
# @lc app=leetcode.cn id=238 lang=python3
#
# [238] 除自身以外数组的乘积
#
from typing import List
# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        for i in range(0, len(nums)):
            if i != 0:
                ans[i] = ans[i - 1] * nums[i - 1]
        r_res = 1
        for i in range(len(nums) - 1, -1, -1):
            if i != len(nums) - 1:
                ans[i] = ans[i] * r_res
            r_res = r_res * nums[i]
        return ans
    # 空间复杂度O(n)
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     leftRes = []
    #     for i in range(0, len(nums)):
    #         if i == 0:
    #             leftRes.append(1)
    #         else:
    #             leftRes.append(leftRes[-1] * nums[i - 1])
    #     rightRes = []
    #     for i in range(len(nums) - 1, -1, -1):
    #         if i == len(nums) - 1:
    #             rightRes.append(1)
    #         else:
    #             rightRes.append(rightRes[-1] * nums[i + 1])
    #     rightRes.reverse()
    #     res = []
    #     for i in range(0, len(nums)):
    #         res.append(leftRes[i] * rightRes[i])
    #     return res
# @lc code=end
print(Solution().productExceptSelf([1,2,3,4]))
