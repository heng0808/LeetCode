#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        ans = 0
        isMinus = False
        if x < 0:
            isMinus = True
            x = -x
        while x / 10 > 0:
            r = x % 10
            x = x // 10
            if ans != 0:
                ans = ans * 10 + r
            else:
                ans = r
        if isMinus:
            ans = -ans
        if ans >= pow(-2, 31) and ans <= (pow(2, 31) - 1):
            return ans
        return 0
# @lc code=end

print(Solution().reverse(120))

