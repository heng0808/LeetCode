#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#
from typing import List
# @lc code=start
class Solution:
    # 记录次数
    def majorityElement(self, nums: List[int]) -> int:
        currentNum, currentCount= nums[0], 1
        for num in nums[1:]:
            if currentCount == 0:
                currentNum = num
                currentCount = 1
            else:
                if num == currentNum:
                    currentCount += 1
                else:
                    currentCount -= 1
        return currentNum
    # 哈希表
    # def majorityElement(self, nums: List[int]) -> int:
    #     table = {}
    #     for num in nums:
    #         if num in table:
    #             table[num] += 1
    #         else:
    #             table[num] = 1
    #     maxcountNum, maxCount = 0, 0
    #     for (num, count) in table.items():
    #         if count > maxCount:
    #             maxcountNum = num
    #             maxCount = count
    #     return maxcountNum
# @lc code=end
print(Solution().majorityElement([5,5]))
