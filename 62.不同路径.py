#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#

# @lc code=start
class Solution:
    # 排列组合
    def uniquePaths(self, m: int, n: int) -> int:
        def factorial(num) -> int:
            res = 1
            for i in range(1, num + 1):
                res = res * i
            return res
        num_m = max(m - 1, n - 1)
        num_n = m - 1 + n - 1
        num_n_factorial = factorial(num_n)
        num_m_factorial = factorial(num_m)
        num_n_m_factorial = factorial(num_n - num_m)
        return num_n_factorial // (num_m_factorial * num_n_m_factorial)
    # 递归
    # def uniquePaths(self, m: int, n: int) -> int:
    #     def lastPath(i, j) -> int:
    #         res = 0
    #         if i == 0 and j == 0:
    #             res = res + 1
    #         if i != 0:
    #             res = res + lastPath(i - 1, j)
    #         if j != 0:
    #             res = res + lastPath(i, j - 1)
    #         return res
    #     ans = lastPath(m - 1, n - 1)
    #     return ans
# @lc code=end
print(Solution().uniquePaths(7, 3))
