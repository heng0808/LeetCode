#
# @lc app=leetcode.cn id=509 lang=python3
#
# [509] 斐波那契数
#

# @lc code=start
class Solution:
    def fib(self, N: int) -> int:
        fib_arr = [0, 1]
        if N < len(fib_arr):
            return fib_arr[N]
        i = 2
        while i <= N:
            ans = fib_arr[0] + fib_arr[1]
            fib_arr[0] = fib_arr[-1]
            fib_arr[1] = ans
            print(str(i) + '->' + str(ans))
            i = i + 1
        return fib_arr[-1] % 1000000007
# @lc code=end
print(Solution().fib(45))