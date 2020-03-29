from typing import List
import sys

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        priceStack = []
        for price in prices:
            if len(priceStack) == 0:
                priceStack.append(price)
            else:
                if len(priceStack) > 1:
                    if price > priceStack[-1]:
                        priceStack.pop()
                        priceStack.append(price)
                    elif price < priceStack[-1]:
                        profit = profit + (priceStack[-1] - priceStack[0])
                        priceStack.pop()
                        priceStack.pop()
                        priceStack.append(price)
                elif len(priceStack) == 1:
                    if price > priceStack[0]:
                        priceStack.append(price)
                    elif price < priceStack[0]:
                        priceStack.pop()
                        priceStack.append(price)
        if len(priceStack) > 1:
            profit = profit + (priceStack[-1] - priceStack[0])
        return profit

print(Solution().maxProfit([7,1,5,3,6,4]))
print(Solution().maxProfit([1,2,3,4,5]))
print(Solution().maxProfit([7,6,4,3,1]))