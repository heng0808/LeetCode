#
# @lc app=leetcode.cn id=1047 lang=python3
#
# [1047] 删除字符串中的所有相邻重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, S: str) -> str:
        index = 0
        stack = []
        while index < len(S):
            if len(stack) > 0:
                if stack[-1] != S[index]:
                    stack.append(S[index])
                else:
                    stack.pop()
            else:
                stack.append(S[index])
            index = index + 1
        return ''.join(stack)
# @lc code=end
print(Solution().removeDuplicates("abbaca"))
