# @Time    : 2018/8/31 下午4:58
# @Author  : 张恒
# @File    : Code3.py
# @Software: PyCharm


class Solution:
    def lengthOfLongestSubstring(self, s) -> int:
        sub_s = ''
        maxSub_s = ''
        for character in s:
            try:
                index = sub_s.index(character)
                if len(sub_s) > len(maxSub_s):
                    maxSub_s = sub_s
                try:
                    sub_s = sub_s[index + 1:]
                except:
                    sub_s = ''
                sub_s = sub_s + character
            except:
                sub_s = sub_s + character
                continue
        length = len(maxSub_s) if len(maxSub_s) > len(sub_s) else len(sub_s)
        return length
if __name__ == '__main__':
    Solution().lengthOfLongestSubstring('aab')