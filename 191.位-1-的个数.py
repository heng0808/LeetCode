#
# @lc app=leetcode.cn id=191 lang=python3
#
# [191] 位1的个数
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            count = count + n % 2
            n = n // 2
        return count
# @lc code=end

print(Solution().hammingWeight(42))
