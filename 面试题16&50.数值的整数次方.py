class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        if n == 0:
            return 1
        elif n == 1:
            return x
        else:
            res = self.myPow(x, n // 2)
            if n % 2 == 1:
                return res * res * x
            else:
                return res * res

print(Solution().myPow(2, 10))