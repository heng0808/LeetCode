class Solution:
    # 斐波那契数列
    # 当前步数等前一步总数加前两补总数
    def numWays(self, n: int) -> int:
        arr = [ i for i in range(0, max(0, n + 1)) ]
        arr[0] = 1
        for i in range(3, n + 1):
            arr[i] = arr[i - 1] + arr[i - 2]
        return arr[-1] % 1000000007
    # 超时
    # def numWays(self, n: int) -> int:
    #     def lastWay(index: int) -> int:
    #         if index == 0:
    #             return 1
    #         else:
    #             ans = 0
    #             if index > 0:
    #                 ans = ans + lastWay(index - 1)
    #             if index > 1:
    #                 ans = ans + lastWay(index - 2)
    #             return ans
    #     return lastWay(n)

print(Solution().numWays(0))