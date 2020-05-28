#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#
from typing import List
# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        nums = [i for i in range(1, n * n + 1)]
        ans = [['' for i in range(n)] for i in range(n)]
        max_i_j = len(ans) - 1
        direction = 0
        s_i, s_j = 0, 0
        e_i, e_j = s_i, max(max_i_j - 1 - s_j, s_j)
        while len(nums) > 0:
            if direction == 0:
                # 左向右
                for j in range(s_j, e_j + 1):
                    ans[s_i][j] = nums.pop(0)
                s_i, s_j = s_i, e_j + 1
                e_i, e_j = max_i_j - s_i - 1, s_j
                direction = 1
            elif direction == 1:
                # 上向下
                for i in range(s_i, e_i + 1):
                    ans[i][s_j] = nums.pop(0)
                s_i, s_j = e_i + 1, e_j
                e_i, e_j = s_i, max_i_j - s_j + 1
                direction = 2
            elif direction == 2:
                # 右向左
                for j in range(s_j, e_j - 1, - 1):
                    ans[s_i][j] = nums.pop(0)
                s_i, s_j = s_i, e_j - 1
                e_i, e_j = max_i_j - s_i + 1, s_j
                direction = 3
            else:
                # 下向上
                for i in range(s_i, e_i - 1, -1):
                    ans[i][s_j] = nums.pop(0)
                s_i, s_j = e_i, e_i
                e_i, e_j = s_i, max(max_i_j - 1 - s_j, s_j)
                direction = 0
        return ans
# @lc code=end
for rows in Solution().generateMatrix(5):
    print(rows)
