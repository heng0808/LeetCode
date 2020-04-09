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
        left, right = 0, -1
        target_dic = Counter(t)
        target_count = len(t)
        find_dic = Counter(t)
        for k in find_dic.keys():
            find_dic[k] = 0
        find_count = 0
        while (left <= right and right < len(s)) or right == -1:
            if find_count == target_count:
                # 找到了合适的
                if m_right == -1 or right - left < m_right - m_left:
                    # 比当前范围小
                    m_left = left
                    m_right = right

            if find_count < target_count:
                # 还没找到->右移窗口
                right = right + 1
                if right < len(s):
                    if s[right] in find_dic:
                        find_dic[s[right]] = find_dic[s[right]] + 1
                        if find_dic[s[right]] <= target_dic[s[right]]:
                            find_count = find_count + 1
            else:
                # 找到了->左移窗口
                if left < len(s):
                    if s[left] in find_dic:
                        find_dic[s[left]] = find_dic[s[left]] - 1
                        if find_dic[s[left]] < target_dic[s[left]]:
                            find_count = find_count - 1
                left = left + 1

        return s[m_left:m_right + 1] if m_right >= m_left else ""                           
# @lc code=end
# print(Solution().minWindow("ADOBECODEBANC", "ABC"))
# print(Solution().minWindow("cabwefgewcwaefgcf", "cae"))
# print(Solution().minWindow("bba", "ab"))
# print(Solution().minWindow("aa", "aa"))