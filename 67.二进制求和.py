#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        ans = ''
        carry = 0
        while i >= 0 or j >= 0:
            res = carry
            if i >= 0:
                res = res + int(a[i])
                i = i - 1
            if j >= 0:
                res = res + int(b[j])
                j = j - 1
            ans = str(res % 2) + ans
            carry = res // 2
        if carry != 0:
            ans = str(carry) + ans
        return ans

# @lc code=end
Solution().addBinary('11','1')
