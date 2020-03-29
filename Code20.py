class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if len(stack)==0:
                stack.append(char)
                continue
            if char=='(' and stack[len(stack) - 1]==')':
                stack.pop()
            elif char==')' and stack[len(stack) - 1]=='(':
                stack.pop()
            elif char=='{' and stack[len(stack) - 1]=='}':
                stack.pop()
            elif char=='}' and stack[len(stack) - 1]=='{':
                stack.pop()
            elif char=='[' and stack[len(stack) - 1]==']':
                stack.pop()
            elif char==']' and stack[len(stack) - 1]=='[':
                stack.pop()
            else:
                stack.append(char)
        return len(stack) == 0

print(Solution().isValid("(]"))