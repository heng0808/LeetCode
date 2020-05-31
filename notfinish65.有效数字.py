#
# @lc app=leetcode.cn id=65 lang=python3
#
# [65] 有效数字
#

# @lc code=start
class Solution:
    def isNumber(self, s: str) -> bool:
        hasPoint = False
        hasE = False
        nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        for i in range(0, len(s)):
            character = s[i]
            if character == '-' or character == '+':
                if i != 0:
                    return False
            if character == 'e':
                if i == 0:
                    return False
                hasPoint = True
                hasE =
            if character == '.':
                if hasPoint:
                    return False
                if i == 0:
                    return False
                if not s[i - 1] in nums:
                    return False
        return True
# @lc code=end

