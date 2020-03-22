# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
# 示例：
# 输入：3
# 输出：3
# 解释： 有三种方法可以爬到楼顶。
# 1. 1 阶 + 1 阶 + 1 阶
# 2. 1 阶 + 2 阶
# 3. 2 阶 + 1 阶

class Solution:
    def climbStairs(self, n: int) -> int:
        def combination(m:int, n:int) -> int:
            n_factorial = 1
            for i in range(1, n + 1):
                n_factorial = n_factorial * i
            m_factorial = 1
            for i in range(1, m + 1):
                m_factorial = m_factorial * i
            n_m_factorial = 1
            for i in range(1, n - m + 1):
                n_m_factorial = n_m_factorial * i
            return int(n_factorial / (m_factorial * n_m_factorial))

        # 两个台阶的个数x
        # 1个台阶的格式n-2x
        # 总的步数n-2x+x=n-x
        # 组合数C(n-2x,n-x)
        ans = 0
        x = 0
        while x * 2 <= n:
            temp = combination(n - 2 * x, n - x)
            ans = ans + temp
            x = x + 1
        return ans

# print(Solution().climbStairs(2))
# print(Solution().climbStairs(3))
print(Solution().climbStairs(4))