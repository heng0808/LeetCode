#
# @lc app=leetcode.cn id=1004 lang=python3
#
# [1004] 最大连续1的个数 III
#
from typing import List
# @lc code=start
class Solution:
    # 自己实现非滑动窗口
    def longestOnes(self, A: List[int], K: int) -> int:
        length = 0
        result = 0
        k_queue = []
        for i in range(0, len(A)):
            num = A[i]
            if num == 0:
                if K > 0:
                    if len(k_queue) == K:
                        left = k_queue.pop(0)
                        A[left] = 0
                        if left > 0 and A[left - 1] == 1:
                            length = i - (left + 1)
                        else:
                            length -= 1
                    A[i] = 1
                    k_queue.append(i)
                    length += 1
                else:
                    length = 0
            elif num == 1:
                length += 1
            if length > result:
                result = length
        return result
    # 滑动窗口，边界算不明白了，放弃。。。
    # def longestOnes(self, A: List[int], K: int) -> int:
    #     left = -1
    #     result = 0
    #     k_count = 0
    #     for i in range(0, len(A)):
    #         if A[i] == 0:
    #             k_count += 1
    #         if k_count > K:
    #             for j in range(left + 1, i):
    #                 if A[j] == 0:
    #                     left = j
    #                     k_count -= 1
    #         if result < i - left:
    #             result = i - left
    #     return result
# @lc code=end
# [1,1,1,0,0,0,1,1,1,1,0]
# [1,1,1,1,0,0,1,1,1,1,0]
# [1,1,1,1,1,0,1,1,1,1,0]
# [1,1,1,0,1,1,1,1,1,1,0]
print(Solution().longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))
print(Solution().longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))
print(Solution().longestOnes([0,0,1,1,1,0,0], 0))
print(Solution().longestOnes([1,1,1,0,0,0,1,1,1,1], 0))
print(Solution().longestOnes([1,0,0,0,1,1,0,0,1,1,0,0,0,0,0,0,1,1,1,1,0,1,0,1,1,1,1,1,1,0,1,0,1,0,0,1,1,0,1,1], 8))
          
# [1,0,0,0,1,1,0,0,1,1,0,0,0,0,0,0,1,1,1,1,0,1,0,1,1,1,1,1,1,0,1,0,1,0,0,1,1,0,1,1]
# [1,0,0,0,1,1,0,0,1,1,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]