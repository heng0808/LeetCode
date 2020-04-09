#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#
from typing import List
# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def nextNum(start:int, combine:List):
            if len(combine) == k:
                combines.append(combine[:])
            else:
                for num in range(start, n+1):
                    combine.append(num)
                    nextNum(num+1, combine)
                    combine.pop()
        combines=[]
        nextNum(1, [])
        return combines
# @lc code=end

print(Solution().combine(4, 2))
