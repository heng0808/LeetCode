#
# @lc app=leetcode.cn id=344 lang=python3
#
# [344] 反转字符串
#
from typing import List
# @lc code=start
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        begin = 0
        end = len(s) - 1
        while begin < end:
            temp = s[begin]
            s[begin] = s[end]
            s[end] = temp
            begin = begin + 1
            end = end - 1
# @lc code=end

