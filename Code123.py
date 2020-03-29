from typing import List
import sys

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        allProfitStack = []
        priceStack = []
        for price in prices:
            if len(priceStack) == 0:
                priceStack.append(price)
            elif len(priceStack) == 1:
                if price < priceStack[0]:
                    priceStack.pop()
                    priceStack.append(price)
                elif price > priceStack[0]:
                    priceStack.append(price)
            else:
                if price > priceStack[-1]:
                    priceStack.pop()
                    priceStack.append(price)
                elif price < priceStack[1]:
                    allProfitStack.append(priceStack)
                    priceStack = [price]

        if len(priceStack) > 1:
            allProfitStack.append(priceStack)
        allProfitStack.sort(key=lambda stack: stack[1] - stack[0], reverse=True)
        profit = 0
        for operation in allProfitStack[:2]:
            profit = profit + (operation[1] - operation[0])
        return profit

# print(Solution().maxProfit([3,3,5,0,0,3,1,4]))
# print(Solution().maxProfit([1,2,3,4,5]))
# print(Solution().maxProfit([7,6,4,3,1]))

