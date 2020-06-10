#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#
from typing import List
# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def nextStep(i, j):
            if grid[i][j] == '0':
                return
            grid[i][j] = '0'
            if i > 0:
                nextStep(i - 1, j)
            if i < len(grid) - 1:
                nextStep(i + 1, j)
            if j > 0:
                nextStep(i, j - 1)
            if j < len(grid[i]) - 1:
                nextStep(i, j + 1)

        res = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] != '0':
                    res += 1
                    nextStep(i, j)
        return res
# @lc code=end
print(Solution().numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))
