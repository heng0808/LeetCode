#
# @lc app=leetcode.cn id=557 lang=python3
#
# [557] 反转字符串中的单词 III
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        left = 0
        right = left
        s_list = list(s)
        while right < len(s_list):
            while right < len(s_list) and s_list[right] != ' ':
                right = right + 1
            n_left = right + 1
            right = right - 1
            while left < right and right < len(s_list):
                character = s_list[left]
                s_list[left] = s_list[right]
                s_list[right] = character
                left = left + 1
                right = right - 1
            left = n_left
            right = left
        return ''.join(s_list)
# @lc code=end
print(Solution().reverseWords("Let's take LeetCode contest"))

