#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        s = '#'.join(s)
        ans = []
        for index in range(0, len(s)):
            left = index
            right = index
            while True:
                if left - 1 >= 0 and right + 1 < len(s):
                    if s[left - 1] == s[right + 1]:
                        left = left - 1
                        right = right + 1
                    else:
                        break
                else:
                    break
            if len(ans) == 0:
                ans = [left, right]
            else:
                length = right - left
                if s[right] == '#':
                    length = length - 2
                if ans[1] - ans[0] <= length:
                    ans = [left, right]
        if len(ans) > 0:
            sub = s[ans[0]:ans[1] + 1]
            return sub.replace('#', '')
        else:
            return ''
# @lc code=end

print(Solution().longestPalindrome("cbbd"))