from typing import List
class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix) - 1, -1, -1):
            if len(matrix[i]) > 0 and matrix[i][0] <= target:
                res, left, right = False, 0, len(matrix[i]) - 1
                while left <= right:
                    mid = (left + right) // 2
                    if matrix[i][mid] > target:
                        right = mid - 1
                    elif matrix[i][mid] < target:
                        left = mid + 1
                    else:
                        res = True
                        break
                if res:
                    return True
        return False

# print(Solution().findNumberIn2DArray([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5))
print(Solution().findNumberIn2DArray([[]], 1))