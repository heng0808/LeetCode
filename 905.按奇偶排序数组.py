#
# @lc app=leetcode.cn id=905 lang=python3
#
# [905] 按奇偶排序数组
#
from typing import List
# @lc code=start
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        l_index = 0
        r_index = len(A) - 1
        while l_index < r_index:
            if A[l_index] % 2 == 1 and A[r_index] % 2 == 0:
                # 交换
                A[l_index] = A[l_index] + A[r_index]
                A[r_index] = A[l_index] - A[r_index]
                A[l_index] = A[l_index] - A[r_index]
                l_index = l_index + 1
                r_index = r_index - 1
            elif A[l_index] % 2 != 1:
                l_index = l_index + 1
            elif A[r_index] % 2 != 0:
                r_index = r_index - 1
        return A
# @lc code=end
print(Solution().sortArrayByParity([3,1,2,4]))
