#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: []):
        ans = ''
        index = 0
        while True:
            character = None
            for _str in strs:
                if index < len(_str):
                    if character == None:
                        character = _str[index]
                    else:
                        if character != _str[index]:
                            character = None
                            break
                else:
                    character = None
                    break
            if character == None:
                break
            else:
                ans = ans + character
            index = index + 1
        return ans
# @lc code=end
print(Solution().longestCommonPrefix(["aa","a"]))

