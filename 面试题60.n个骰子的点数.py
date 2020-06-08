from typing import List

class Solution:
    # 动态规划
    # 考虑边界
    # dp[n][j] = 1.6667 * (dp[n-1][j-1] + ... + dp[n-1][j-6])
    def twoSum(self, n: int) -> List[float]:
        dp = []
        for k in range(1, n + 1):
            dp.append([1 / 6] * (6 * k + 1))
            for j in range(k, len(dp[-1])):
                p = 0
                for i in range(1, 6 + 1):
                    if k - 1 - 1 >= 0 and j - i >= k - 1 and j - i <= (k - 1) * 6: 
                        p += dp[k - 2][j - i]
                if p != 0:
                    dp[k - 1][j] = dp[k - 1][j] * p
        return [round(p, 5) for p in dp[-1][n:]]

print(Solution().twoSum(1))