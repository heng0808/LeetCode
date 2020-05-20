#
# @lc app=leetcode.cn id=43 lang=python3
#
# [43] 字符串相乘
#

# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        else:
            if num1 == '1':
                return num2
            if num2 == '1':
                return num1
        ans = ""
        for i in range(0, len(num1)):
            charcter1 = num1[len(num1) - i - 1]
            res = ""
            tenth = 0
            for j in range(0, len(num2)):
                charcter2 = num2[len(num2) - j - 1]
                product = int(charcter1) * int(charcter2) + tenth
                first = product % 10
                res = str(first) + res
                tenth = int(product / 10)
            res = ('' if tenth == 0 else str(tenth)) + res
            for k in range(0, i):
                res = res + '0'
            ans = self.add(ans, res)
        return ans


    def add(self, num1: str, num2:str) -> str:
        if len(num1) == 0 and len(num2) == 0:
            return ""
        elif len(num1) == 0:
            return num2
        elif len(num2) == 0:
            return num1
        ans = ""
        tenth = 0
        index = 0
        while True:
            charcter1 = num1[len(num1) - index - 1]
            charcter2 = num2[len(num2) - index - 1]
            sum = int(charcter1) + int(charcter2) + tenth
            first = sum % 10
            ans = str(first) + ans
            tenth = int(sum / 10)
            index = index + 1
            if index == min(len(num1), len(num2)):
                header = ""
                if index < len(num1):
                    header = num1[:len(num1) - index]
                if index < len(num2):
                    header = num2[:len(num2) - index]
                if tenth != 0:
                    header = self.add(header, str(tenth))
                ans = header + ans
                break
        return ans
# @lc code=end

