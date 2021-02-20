#
# @lc app=leetcode.cn id=1004 lang=python3
#
# [1004] 最大连续1的个数 III
#
from typing import List
# @lc code=start
class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        def _longestOnes(_A: List[int]) -> int:
            length = 0
            result = 0
            k_queue = []
            for i in range(0, len(_A)):
                num = _A[i]
                if num == 0:
                    if K > 0:
                        if len(k_queue) == K:
                            left = k_queue.pop(0)
                            _A[left] = 0
                            if left > 0 and _A[left - 1] == 1:
                                length = len(k_queue)
                            else:
                                length -= 1
                        _A[i] = 1
                        k_queue.append(i)
                        length += 1
                    else:
                        length = 0
                elif num == 1:
                    length += 1
                if length > result:
                    result = length
            return result
        l_result = _longestOnes(A)
        r_result = _longestOnes(list(reversed(A)))
        return max(l_result, r_result)
# @lc code=end
# [1,1,1,0,0,0,1,1,1,1,0]
# [1,1,1,1,0,0,1,1,1,1,0]
# [1,1,1,1,1,0,1,1,1,1,0]
# [1,1,1,0,1,1,1,1,1,1,0]
# print(Solution().longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))
print(Solution().longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))
# print(Solution().longestOnes([0,0,1,1,1,0,0], 0))
# print(Solution().longestOnes([1,1,1,0,0,0,1,1,1,1], 0))
# print(Solution().longestOnes([1,0,0,0,1,1,0,0,1,1,0,0,0,0,0,0,1,1,1,1,0,1,0,1,1,1,1,1,1,0,1,0,1,0,0,1,1,0,1,1], 8))

