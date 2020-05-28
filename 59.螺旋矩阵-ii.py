#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#
from typing import List
# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        arr = [['' for i in range(n)] for i in range(n)]
        arr[0][0] = 1
        i, j = 0, 0
        while True:
            arr[i][j]
        return arr
# @lc code=end
print(Solution().generateMatrix(3))
