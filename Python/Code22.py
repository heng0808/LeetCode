class Solution:
    def generateParenthesis(self, n: int) -> [str]:
        parenthesis = []
        def append(current:str, sign:str, leftcount:int, rightcount:int):
            current = current + sign
            if len(current) < 2 * n:
                append(current, '(', leftcount, rightcount)
                append(current, ')', leftcount, rightcount)
            else:
                parenthesis.append(current)
        if n == 0:
            return parenthesis
        else:
            append('', '', 0, 0)
            return parenthesis
        # parenthesis = []
        # def append(current:str, sign:str, leftcount:int, rightcount:int):
        #     if sign == '(':
        #         leftcount = leftcount + 1
        #     else:
        #         rightcount = rightcount + 1
        #     current = current + sign
        #     if rightcount <= leftcount:
        #         if leftcount < n and rightcount < n:
        #             append(current, '(', leftcount, rightcount)
        #             append(current, ')', leftcount, rightcount)
        #         elif leftcount < n:
        #             append(current, '(', leftcount, rightcount)
        #         elif rightcount < n:
        #             append(current, ')', leftcount, rightcount)
        #         else:
        #             parenthesis.append(current)
        # if n == 0:
        #     return parenthesis
        # else:
        #     append('', '(', 0, 0)
        #     return parenthesis

print(Solution().generateParenthesis(3))
print(len(Solution().generateParenthesis(3)))