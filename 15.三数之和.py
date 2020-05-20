#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
from typing import List
# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        if len(nums) < 3:
            return []
        if nums[0] > 0:
            return []
        if nums[len(nums) - 1] < 0:
            return []
        if nums[0] == nums[len(nums) - 1] and nums[0] == 0:
            return [[0, 0, 0]]
        resultSet = set()
        for index in range(0, len(nums)):
            num1 = nums[index]
            if num1 > 0:
                break
            left = index + 1
            right = len(nums) - 1
            while left < right:
                num2 = nums[left]
                num3 = nums[right]
                sum = num2 + num3
                if sum > -num1:
                    right = right - 1
                elif sum < -num1:
                    left = left + 1
                else:
                    resultSet.add(str([num1, num2, num3]))
                    left = left + 1
                    right = right - 1
        resultList = []
        for resultStr in resultSet:
            resultList.append(eval(resultStr))
        return resultList
# @lc code=end

