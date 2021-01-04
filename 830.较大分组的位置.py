#
# @lc app=leetcode.cn id=830 lang=python3
#
# [830] 较大分组的位置
#
from typing import List
# @lc code=start
class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        res = []
        l = -1
        c = None
        for i in range(0, len(s)):
            if l == -1:
                c = s[i]
                l = i
            elif c != s[i]:
                if i - l >= 3:
                    res.append([l, i - 1])
                c = s[i]
                l = i
        if l != -1 and l < len(s) and len(s) - l >= 3:
            res.append([l, len(s) - 1])
        return res
# @lc code=end
# print(Solution().largeGroupPositions('abbxxxxzzy'))
# print(Solution().largeGroupPositions('abc'))
# print(Solution().largeGroupPositions('abcdddeeeeaabbbcd'))
# print(Solution().largeGroupPositions('aba'))
print(Solution().largeGroupPositions('aaa'))