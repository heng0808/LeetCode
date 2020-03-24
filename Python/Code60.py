# 给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。
# 按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：
#     1. "123"
#     2. "132"
#     3. "213"
#     4. "231"
#     5. "312"
#     6. "321"
# 给定 n 和 k，返回第 k 个排列。
# 说明：
#     - 给定 n 的范围是 [1, 9]。
#     - 给定 k 的范围是[1,  n!]。
# 示例:  
#     输入: n = 3, k = 3
#     输出: "213"

from functools import reduce
from math import ceil

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [i for i in range(1, n+1)]
        counts = []
        for num in nums:
            if len(counts) == 0:
                counts.append(num)
            else:
                counts.append(counts[-1] * num)
        ans = ''
        while len(ans) < n:
            count = counts.pop()
            piece = count / len(nums)
            index = ceil(k / piece) - 1
            k = k % piece
            num = nums[index]
            del nums[index]
            ans = ans + str(num)
        return ans

print(Solution().getPermutation(4,9))