#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#

# @lc code=start
class Solution:
    # 找规律：行先降低在升高再降低
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1:
            return s
        arr = ['' for i in range(0, numRows)]
        asc, row = True, 0
        for character in s:
            arr[row] = arr[row] + character
            if asc:
                if row == numRows - 1:
                    asc = False
                    row = row - 1
                else:
                    row = row + 1
            else:
                if row == 0:
                    asc = True
                    row = row + 1
                else:
                    row = row - 1
        ans = ''.join(arr)
        # P   A
        # A P L
        # Y   I
        return ans
    # 二维数组 很蠢
    # def convert(self, s: str, numRows: int) -> str:
    #     if numRows <= 1:
    #         return s
    #     arr = []
    #     count = len(s)
    #     row = 0
    #     s_i = 0
    #     while count > 0 and s_i < len(s):
    #         arr.append([])
    #         if row % (numRows - 1) == 0:
    #             while len(arr[-1]) < numRows:
    #                 arr[-1].append('')
    #                 if s_i < len(s):
    #                     arr[-1][-1] = s[s_i]
    #                 s_i = s_i + 1
    #             count = count - min(len(s) - s_i, numRows)
    #         else:
    #             col = row % (numRows - 1)
    #             while len(arr[-1]) < numRows:
    #                 arr[-1].append('')
    #                 if len(arr[-1]) == numRows - col:
    #                     arr[-1][-1] = s[s_i]
    #             s_i = s_i + 1
    #             count = count - 1
    #         row = row + 1
    #     ans = ''
    #     for i in range(0, numRows):
    #         for j in range(0, len(arr)):
    #             ans = ans + arr[j][i]
    #     return ans
# @lc code=end
# print(Solution().convert('ABC', 2))
print(Solution().convert('PAYPALISHIRING', 3))
# print(Solution().convert('LEETCODEISHIRING', 3))
# print(Solution().convert('LEETCODEISHIRING', 4))
# print(Solution().convert('LEETCODEISHIRING', 5))