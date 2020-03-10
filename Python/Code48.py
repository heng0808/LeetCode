from typing import List

class Solution:
    def rotate1(self, matrix: List[List[int]]) -> None:
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

    def rotate2(self, matrix: List[List[int]]) -> None:
        for i in range(0, len(matrix)):
            for j in range(i, len(matrix)):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        for i in range(0, len(matrix)):
            matrix[i].reverse()

# 先转置，再求逆矩
# [[ 1, 2, 3, 4],
#  [ 5, 6, 7, 8],
#  [ 9,10,11,12],
#  [13,14,15,16]]
# ----------
# [[1,4,7],
#  [2,5,8],
#  [3,6,9]]
# ----------
# [[7,4,1],
#  [8,5,2],
#  [9,6,3]]


# matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix = [[ 1, 2, 3, 4],[ 5, 6, 7, 8],[ 9,10,11,12],[13,14,15,16]]

Solution().rotate2(matrix)

print(matrix)