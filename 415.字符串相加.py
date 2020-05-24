#
# @lc app=leetcode.cn id=415 lang=python3
#
# [415] 字符串相加
#

# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i = len(num1) - 1
        j = len(num2) - 1
        ans = 0
        res = ''
        while i >= 0 or j >= 0:
            if i >= 0:
                ans = ans + int(num1[i])
                i = i - 1
            if j >= 0:
                ans = ans + int(num2[j])
                j = j - 1
            res = str(ans % 10) + res
            ans = ans // 10
        if ans > 0:
            res = str(ans) + res
        return res
# @lc code=end
print(Solution().addStrings('51189', '967895'))

