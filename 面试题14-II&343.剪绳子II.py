class Solution:
    def cuttingRope(self, n: int) -> int:
        if n <= 3:
            return n - 1
        a, b = n // 3, n % 3
        if b == 0:
            return pow(3, a) % 1000000007
        if b == 1:
            return pow(3, a - 1) * 4 % 1000000007
        return pow(3, a) * 2 % 1000000007