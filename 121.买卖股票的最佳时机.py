from typing import List
import sys
class Solution:
    # Soltion 1
    # def maxProfit(self, prices: List[int]) -> int:
    #     left = 0
    #     profit = 0
    #     while left < len(prices) - 1:
    #         for i in range(left + 1, len(prices), 1):
    #             profit = max(profit, prices[i] - prices[left])
    #         left = left + 1
    #     return profit

    # Soltion 2
    def maxProfit(self, prices: List[int]) -> int:
        minPiece = sys.maxsize
        profit = 0
        for piece in prices:
            if piece < minPiece:
                minPiece = piece
            elif piece - minPiece > profit:
                profit = piece - minPiece
        return 0 if profit == sys.maxsize else profit

print(Solution().maxProfit([7,1,5,3,6,4]))
# print(Solution().maxProfit([7,6,4,3,1]))