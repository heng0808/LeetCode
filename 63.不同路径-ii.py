#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#
from typing import List
# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        for i in range(0, len(obstacleGrid)):
            for j in range(0, len(obstacleGrid[i])):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                else:
                    if i == 0 and j == 0:
                        obstacleGrid[i][j] = 1
                    else:
                        if i != 0 and obstacleGrid[i - 1][j] != -1:
                            obstacleGrid[i][j] = obstacleGrid[i][j] + obstacleGrid[i - 1][j]
                        if j != 0 and obstacleGrid[i][j - 1] != -1:
                            obstacleGrid[i][j] = obstacleGrid[i][j] + obstacleGrid[i][j - 1]
        return obstacleGrid[-1][-1]
# @lc code=end
print(Solution().uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))
