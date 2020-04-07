#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#

from typing import List

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        row_count = len(matrix)
        col_count = len(matrix[0])
        left_index = 0
        right_index = row_count * col_count - 1
        while left_index <= right_index:
            if matrix[left_index//col_count][left_index%col_count] == target:
                return True
            elif matrix[right_index//col_count][right_index%col_count] == target:
                return True
            elif right_index - left_index <= 1:
                break
            else:
                mid_index = (left_index + right_index) // 2
                if matrix[mid_index//col_count][mid_index%col_count] < target:
                    left_index = mid_index
                else:
                    right_index = mid_index
        return False
# @lc code=end
print(Solution().searchMatrix([[1,   3,  5,  7],[10, 11, 16, 20],[23, 30, 34,50]], 13))