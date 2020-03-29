class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        elif n < 0:
            n = -n
            x = 1.0 / x
        ans = 1
        temp = x
        count = 1
        while count < n:
            if n >= count * 2:
                temp = temp * temp
                count = count * 2
            else:
                ans = ans * temp
                n = n - count
                if n > 0:
                    temp = x
                    count = 1
                else:
                    temp = 1
                    count = 0
        return ans * temp

# print(Solution().myPow(2.00000, 32))
# print(Solution().myPow(2.00000, -2))
print(Solution().myPow(0.00001, 2147483647))