#
# @lc app=leetcode.cn id=697 lang=python3
#
# [697] 数组的度
#
from typing import List
# @lc code=start
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        # 1、找最大的度
        # 2、找最短的序列
        mapping = {}
        for i in range(0, len(nums)):
            num = nums[i]
            if num in mapping:
                mapping[num][0] += 1
                mapping[num][2] = i
            else:
                mapping[num] = [1, i, i]
        result = nums[0]
        for (key, (c, i, j)) in mapping.items():
            if c > mapping[result][0]:
                result = key
            elif c == mapping[result][0]:
                if j - i < mapping[result][2] - mapping[result][1]:
                    result = key
        return mapping[result][2] - mapping[result][1] + 1
# @lc code=end

print(Solution().findShortestSubArray([1, 2, 2, 3, 1]))
print(Solution().findShortestSubArray([1,2,2,3,1,4,2]))

