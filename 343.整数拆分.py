#
# @lc app=leetcode.cn id=343 lang=python3
#
# [343] 整数拆分
#

# @lc code=start
class Solution:
    # def integerBreak(self, n: int) -> int:
    #     dp = [1] * (n + 1)
    #     for i in range(3, n + 1):
    #         for j in range(1, i):
    #             dp[i] = max(dp[i], j * dp[i - j], j * (i - j))
    #     return dp[n]
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n - 1
        a, b = n // 3, n % 3
        if b == 0:
            return pow(3, a)
        if b == 1:
            return pow(3, a - 1) * 4
        return pow(3, a) * 2

# @lc code=end

print(Solution().integerBreak(10))
# 3 2
# 4 4
# 5 6
# 6 9
# 7 12
