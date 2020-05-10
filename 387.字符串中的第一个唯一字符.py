#
# @lc app=leetcode.cn id=387 lang=python3
#
# [387] 字符串中的第一个唯一字符
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        charactorCount = {}
        for charactor in s:
            if charactor in charactorCount.keys():
                charactorCount[charactor] = charactorCount[charactor] + 1
            else:
                charactorCount[charactor] = 1
        for index in range(0, len(s)):
            if charactorCount[s[index]] == 1:
                return index
        return -1
# @lc code=end
print(Solution().firstUniqChar("leetcode"))
print(Solution().firstUniqChar("loveleetcode"))
