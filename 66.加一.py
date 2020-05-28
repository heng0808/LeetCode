#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#
from typing import List
# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        numTen = 0
        digits[-1] = digits[-1] + 1
        for i in range(len(digits) - 1, -1, -1):
            digits[i] = digits[i] + numTen
            numTen = digits[i] // 10
            digits[i] = digits[i] % 10
        if numTen > 0:
            digits.insert(0, numTen)
        return digits
# @lc code=end
Solution().plusOne([9,9,9])

