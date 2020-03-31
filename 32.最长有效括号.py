class Solution:
    def longestValidParentheses(self, s: str) -> int:
        maxlength = 0
        leftcount = 0
        rightcount = 0
        for index in range(0, len(s)):
            if s[index] == '(':
                leftcount = leftcount + 1
            else:
                rightcount = rightcount + 1
            if rightcount == leftcount:
                maxlength = max(maxlength, leftcount + rightcount)
            elif rightcount > leftcount:
                leftcount = 0
                rightcount = 0

        rightcount = 0
        leftcount = 0
        for index in reversed(range(0, len(s))):
            if s[index] == ')':
                rightcount = rightcount + 1
            else:
                leftcount = leftcount + 1
            if rightcount == leftcount:
                maxlength = max(maxlength, rightcount + leftcount)
            elif leftcount > rightcount:
                leftcount = 0
                rightcount = 0
        return maxlength

        # maxlength = 0
        # stack = [-1]
        # for index in range(0, len(s)):
        #     if s[index] == '(':
        #         stack.append(index)
        #     else:
        #         stack.pop()
        #         if len(stack) == 0:
        #             stack.append(index)
        #         else:
        #             maxlength = max(maxlength, index - stack[-1])
        return maxlength
# print(Solution().longestValidParentheses("()()"))
# print(Solution().longestValidParentheses(")()())"))
# print(Solution().longestValidParentheses("(()"))
# print(Solution().longestValidParentheses("()"))
print(Solution().longestValidParentheses(")()(((())))("))
# print(Solution().longestValidParentheses("()((())"))