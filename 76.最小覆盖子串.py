#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#
from collections import Counter
# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m_left, m_right = 0, -1
        left, right = 0, 0
        target_dic = Counter(t)
        target_count = len(t)
        find_dic = Counter(t)
        for k in find_dic.keys():
            find_dic[k] = 0
        find_count = 0
        while left <= right and right < len(s):
            if (m_right == -1 or m_right - m_left > left - right) and find_count == target_count:
                m_left = left
                m_right = right
            if find_count < target_count:
                right = right + 1
                if right < len(s) and s[right] in find_dic and find_dic[s[right]] < target_dic[s[right]]:
                    find_dic[s[right]] = find_dic[s[right]] + 1
                    find_count = find_count + 1
            else:
                left = left + 1
                if left < len(s) and s[left] in find_dic and find_dic[s[left]] > 0:
                    find_dic[s[left]] = find_dic[s[left]] - 1
                    find_count = find_count - 1

        return s[m_left:m_right + 1] if m_right >= m_left else ""                           
# @lc code=end
print(Solution().minWindow("ADOBECODEBANC", "ABC"))
# print(Solution().minWindow("cabwefgewcwaefgcf", "cae"))
# print(Solution().minWindow("bba", "ab"))
# print(Solution().minWindow("aa", "aa"))