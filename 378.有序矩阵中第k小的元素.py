#
# @lc app=leetcode.cn id=378 lang=python3
#
# [378] 有序矩阵中第K小的元素
#
from typing import List
# @lc code=start
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        row = len(matrix)
        col = len(matrix[0])
        left = matrix[0][0]
        right = matrix[row - 1][col - 1]
        while left < right:
            mid = (left + right) // 2
            count = self.findNotBiggerThanMid(matrix, mid, row, col)
            if count < k:
                left = mid + 1
            else:
                right = mid 
        return right

    def findNotBiggerThanMid(self, matrix: List[List[int]], mid, row: int, col: int) -> int:
        i = row - 1
        j = 0
        count = 0
        while i >= 0 and j < col:
            num = matrix[i][j]
            if num <= mid:
                count = count + i + 1
                j = j + 1
            else:
                i = i - 1
        return count
# @lc code=end

print(Solution().kthSmallest([[ 1,  5,  9],[10, 11, 13],[12, 13, 15]], 8))

