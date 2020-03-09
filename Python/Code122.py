from typing import List
import sys

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        priceQueue = []
        for price in prices:
            if len(priceQueue) == 0:
                priceQueue.append(price)
            else:
                if len(priceQueue) > 1:
                    if price > priceQueue[-1]:
                        priceQueue.pop()
                        priceQueue.append(price)
                    elif price < priceQueue[-1]:
                        profit = profit + (priceQueue[-1] - priceQueue[0])
                        priceQueue.pop()
                        priceQueue.pop()
                        priceQueue.append(price)
                elif len(priceQueue) == 1:
                    if price > priceQueue[0]:
                        priceQueue.append(price)
                    elif price < priceQueue[0]:
                        priceQueue.pop()
                        priceQueue.append(price)
        if len(priceQueue) > 1:
            profit = profit + (priceQueue[-1] - priceQueue[0])
        return profit

print(Solution().maxProfit([7,1,5,3,6,4]))
print(Solution().maxProfit([1,2,3,4,5]))
print(Solution().maxProfit([7,6,4,3,1]))