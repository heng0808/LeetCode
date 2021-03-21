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
        # Solution1 O(m+n)
        # rows = set()
        # cols = set()
        # for i in range(0, len(matrix)):
        #     for j in range(0, len(matrix[0])):
        #         if matrix[i][j] == 0:
        #             rows.add(i)
        #             cols.add(j)

        # for i in range(0, len(matrix)):
        #     for j in range(0, len(matrix[0])):
        #         if (i in rows or j in cols) and matrix[i][j] != 0:
        #             matrix[i][j] = 0

        # Solution2 O(1)
        row = len(matrix)
        col= len(matrix[0])
        row0_zero = False # 记录第一行是否有0
        col0_zero = False # 记录第一列是否有0
        for i in range(0, col):
            if matrix[0][i] == 0:
                row0_zero = True

        for i in range(0, row):
            if matrix[i][0] == 0:
                col0_zero = True

        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        for i in range(1, row):
            for j in range(1, col):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

        if row0_zero:
            for i in range(0, col):
                matrix[0][i] = 0
        if col0_zero:
            for i in range(0, row):
                matrix[i][0] = 0
        

# @lc code=end


matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Solution().setZeroes(matrix)
print(matrix)