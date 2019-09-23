# class Solution:
#     def generateParenthesis(self, n: int) -> [str]:
#         parenthesis = []
#         def append(current:str, sign:str, leftcount:int, rightcount:int):
#             if sign == '(':
#                 leftcount = leftcount + 1
#             else:
#                 rightcount = rightcount + 1
#             current = current + sign
#             if rightcount <= leftcount:
#                 if leftcount < n and rightcount < n:
#                     append(current, '(', leftcount, rightcount)
#                     append(current, ')', leftcount, rightcount)
#                 elif leftcount < n:
#                     append(current, '(', leftcount, rightcount)
#                 elif rightcount < n:
#                     append(current, ')', leftcount, rightcount)
#                 else:
#                     parenthesis.append(current)
#         if n == 0:
#             return parenthesis
#         else:
#             append('', '(', 0, 0)
#             return parenthesis

class Solution(object):
    def generateParenthesis(self, N):
        ans = []
        def backtrack(S = '', left = 0, right = 0):
            if len(S) == 2 * N:
                ans.append(S)
                return
            if left < N:
                backtrack(S+'(', left+1, right)
            if right < left:
                backtrack(S+')', left, right+1)

        backtrack()
        return ans

result = Solution().generateParenthesis(3)
print(len(result))
print(result)