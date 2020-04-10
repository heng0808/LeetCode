#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#
from typing import List
# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        _sets = [[]]
        _set = []
        def nextNum(first:int):
            if len(_set) > 0:
                _sets.append(_set[:])
            if len(_set) == len(nums):
                return
            for i in range(first, len(nums)):
                _set.append(nums[i])
                nextNum(i+1)
                _set.pop()
        nextNum(0)
        return _sets
# @lc code=end
print(Solution().subsets([1,2,3]))

