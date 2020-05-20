#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, str: str) -> int:
        isnegative = False
        num = None
        first_letter = None
        for index in range(0, len(str)):
            _ascii = ord(str[index])
            if first_letter == None:
                if _ascii == 32:
                    continue
                if _ascii >= 48 and _ascii <= 57:
                    num = int(chr(_ascii))
                    first_letter = str[index]
                    continue
                if _ascii == 45:
                    isnegative = True
                    first_letter = str[index]
                    continue
                if _ascii == 43:
                    first_letter = str[index]
                    continue
                break
            else:
                if _ascii >= 48 and _ascii <= 57:
                    if num == None:
                        num = int(chr(_ascii))
                    else:
                        num = num * 10 + int(chr(_ascii))
                    if isnegative:
                        if num > pow(2, 31):
                            return 0 - pow(2, 31)
                    else:
                        if num > (pow(2, 31) - 1):
                            return pow(2, 31) - 1
                    continue
                break
        if first_letter == None:
            return 0
        else:
            if num == None:
                return 0
            else:
                if isnegative:
                    return 0 - num
                else:
                    return num
# @lc code=end
print(Solution().myAtoi("42"))
