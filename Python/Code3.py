# @Time    : 2018/8/31 下午4:58
# @Author  : 张恒
# @File    : Code3.py
# @Software: PyCharm


class Solution:
    def lengthOfLongestSubstring(self, s) -> int:
        if len(s) < 2:
            return len(s)
        left = 0
        right = 1
        lookup = {s[left]: 1}
        max_len = 0
        while right < len(s):
            character = s[right]
            if character in lookup and lookup[character] > 0:
                # 当前窗口存在该字符
                max_len = max(max_len, right - left)
                while lookup[character] > 0:
                    remove_character = s[left]
                    if remove_character in lookup:
                        lookup[remove_character] = lookup[remove_character] - 1
                    left = left + 1
            else:
                right = right + 1
                lookup[character] = 1
        return max(max_len, right - left)

print(Solution().lengthOfLongestSubstring("ab"))
print(Solution().lengthOfLongestSubstring('abcabcbb'))
print(Solution().lengthOfLongestSubstring('pwwkew'))
print(Solution().lengthOfLongestSubstring(''))
print(Solution().lengthOfLongestSubstring('abcdefg'))