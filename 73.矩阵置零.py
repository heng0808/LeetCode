#
# @lc app=leetcode.cn id=73 lang=python3
#
# [73] 矩阵置零
#

from typing import List

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = set()
        cols = set()
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                if (i in rows or j in cols) and matrix[i][j] != 0:
                    matrix[i][j] = 0
# @lc code=end


matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Solution().setZeroes(matrix)
print(matrix)