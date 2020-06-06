class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        char_index = {}
        i, j = 0, 0
        while j < len(s):
            if s[j] in char_index and char_index[s[j]] >= i:
                ans = max(ans, j - i)
                i = char_index[s[j]] + 1
            char_index[s[j]] = j
            j += 1
        return max(ans, j - i)

print(Solution().lengthOfLongestSubstring('abba'))