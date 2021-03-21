#
# @lc app=leetcode.cn id=150 lang=python3
#
# [150] 逆波兰表达式求值
#
from typing import List
# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '+':
                num1 = stack.pop()
                num0 = stack.pop()
                stack.append(num0 + num1)
                continue
            if token == '-':
                num1 = stack.pop()
                num0 = stack.pop()
                stack.append(num0 - num1)
                continue
            if token == '*':
                num1 = stack.pop()
                num0 = stack.pop()
                stack.append(num0 * num1)
                continue
            if token == '/':
                num1 = stack.pop()
                num0 = stack.pop()
                stack.append(int(num0 / num1))
                continue
            stack.append(int(token))            
        return stack[0]
# @lc code=end
# print(Solution().evalRPN(["2","1","+","3","*"]))
# print(Solution().evalRPN(["4","13","5","/","+"]))
print(Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
