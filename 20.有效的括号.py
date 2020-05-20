#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for character in s:
            stack.append(character)
            if character == ')':
                if len(stack) > 1 and stack[-2] == '(':
                    stack.pop()
                    stack.pop()
                else:
                    break
            elif character == '}':
                if len(stack) > 1 and stack[-2] == '{':
                    stack.pop()
                    stack.pop()
                else:
                    break
            elif character == ']':
                if len(stack) > 1 and stack[-2] == '[':
                    stack.pop()
                    stack.pop()
                else:
                    break
        return len(stack) == 0
# @lc code=end
print(Solution().isValid("]"))

