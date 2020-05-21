#
# @lc app=leetcode.cn id=135 lang=python3
#
# [135] 分发糖果
#
from typing import List
# @lc code=start
class Solution:
    def candy(self, ratings: List[int]) -> int:
        l2r = [1] * len(ratings)
        for i in range(0, len(ratings)):
            if i > 0 and ratings[i] > ratings[i - 1]:
                l2r[i] = l2r[i - 1] + 1
        r2l = [1] * len(ratings)
        for i in range(len(ratings) - 1, -1, -1):
            if i < len(ratings) - 1 and ratings[i] > ratings[i + 1]:
                r2l[i] = r2l[i + 1] + 1
        ans = 0
        for i in range(0, len(ratings)):
            ans = ans + max(l2r[i], r2l[i])
        return ans
    # Time Limit
    # def candy(self, ratings: List[int]) -> int:
    #     candies = [1] * len(ratings)
    #     flag = True
    #     while flag:
    #         flag = False
    #         for i in range(0, len(ratings)):
    #             # 判断是否比左边大
    #             if i > 0 and ratings[i] > ratings[i - 1] and candies[i] <= candies[i - 1]:
    #                 candies[i] = candies[i - 1] + 1
    #                 flag = True
    #             # 判断是否比右边大
    #             if i < len(ratings) - 1 and ratings[i] > ratings[i + 1] and candies[i] <= candies[i + 1]:
    #                 candies[i] = candies[i + 1] + 1
    #                 flag = True
    #     ans = 0
    #     for candy in candies:
    #         ans = ans + candy
    #     return ans
# @lc code=end
print(Solution().candy([1,2,2]))
