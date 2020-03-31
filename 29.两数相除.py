class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = (dividend > 0) ^ (divisor > 0)
        def isPositiveNum(num: int) -> bool:
            return num >= 0
        def isNegativeNum(num: int) -> bool:
            return num < 0
        num1 = abs(dividend)
        num2 = abs(divisor)
        pre_count = 0
        temp_count = 0
        while num1 - num2 - temp_count * num2 - pre_count * num2 >= 0:
            if temp_count == 0:
                temp_count = temp_count + 1
            else:
                if num1 - (temp_count * 2) * num2 - pre_count * num2 >= 0:
                    temp_count = temp_count + temp_count
                else:
                    pre_count = pre_count + temp_count
                    temp_count = 0
        count = pre_count + temp_count
        if isPositiveNum(dividend) and isPositiveNum(divisor):
            return count
        elif isNegativeNum(dividend) and isNegativeNum(divisor):
            return count if count < 2**31 else count-1
        else:
            return -count
print(Solution().divide(dividend=-2147483648, divisor=-1))