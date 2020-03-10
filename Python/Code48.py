from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        level = 0
        length = len(matrix) - 1
        count = len(matrix)
        while count > 1:
            for i in range(0, count - 1):
                i1 = matrix[level][i + level]
                i2 = matrix[i + level][length - level]
                i3 = matrix[length - level][length - i - level]
                i4 = matrix[length - i - level][level]
                matrix[level][i + level] = i4
                matrix[i + level][length - level] = i1
                matrix[length - level][length - i - level] = i2
                matrix[length - i - level][level] = i3
            count = count - 2
            level = level + 1

# matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix = [[ 5, 1, 9,11],[ 2, 4, 8,10],[13, 3, 6, 7],[15,14,12,16]]

Solution().rotate(matrix)

print(matrix)