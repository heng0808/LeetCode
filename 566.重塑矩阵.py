#
# @lc app=leetcode.cn id=566 lang=python3
#
# [566] 重塑矩阵
#
from typing import List
# @lc code=start
class Solution:
    # 可以用二维数组的一维表示来做
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(nums) == 0:
            return nums
        if len(nums[0]) == 0:
            return nums
        if len(nums) * len(nums[0]) != r * c:
            return nums
        result = [[]]
        for i in range(0, len(nums)):
            for j in range(0, len(nums[i])):
                if len(result[-1]) < c:
                    result[-1].append(nums[i][j])
                else:
                    result.append([nums[i][j]])
        return result

# @lc code=end
print(Solution().matrixReshape([[1,2], [3,4]], 2, 4))