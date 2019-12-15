class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # 超时
        def isValid(subs:str) -> bool:
            stack = []
            for charactor in subs:
                if charactor == "(":
                    stack.append(charactor)
                elif len(stack) != 0 and stack[-1] == "(":
                    stack.pop()
                else:
                    return False
            return len(stack) == 0
        maxLength = 0
        for i in range(0, len(s)):
            for j in range(i+2, len(s)+1, 2):
                if isValid(s[i:j]):
                    maxLength = max(maxLength, len(s[i:j]))
        return maxLength
print(Solution().longestValidParentheses(")()())"))
# print(Solution().longestValidParentheses("(()"))
# print(Solution().longestValidParentheses("()"))
# print(Solution().longestValidParentheses(")()(((())))("))
# print(Solution().longestValidParentheses("()(()"))