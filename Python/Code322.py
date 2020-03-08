import sys
class Solution:
    def coinChange(self, coins: [int], amount: int) -> int:
        # Solution 1
        # if amount == 0:
        #     return 0
        # coins.sort(reverse=True)
        # compose = []
        # def change(remain:int, round:int):
        #     for i in range(0, len(coins)):
        #         if remain == coins[i]:
        #             compose.append(coins[i])
        #             break
        #         elif remain > coins[i]:
        #             compose.append(coins[i])
        #             if change(remain - coins[i], round + 1) == -1:
        #                 compose.pop()
        #             else:
        #                 break
        #     return -1 if len(compose) < round else compose[-1]
        # if change(amount, 1) == -1:
        #     return -1
        # else:
        #     return len(compose)

        # Solution 2
        # coins.sort(reverse=True)
        # compose = []
        # def change(remain:int, coinIndex:int) -> bool:
        #     if coinIndex >= len(coins):
        #         return False
        #     maxPiece = int(remain / coins[coinIndex])
        #     for count in range(maxPiece, -1, -1):
        #         compose.append(count)
        #         if remain - count * coins[coinIndex] == 0:
        #             return True
        #         elif change(remain - count * coins[coinIndex], coinIndex + 1):
        #             return True
        #         else:
        #             compose.pop()
        #     return False

        # change(amount, 0)
        # return -1 if len(compose) == 0 else sum(compose)

        # Solution 3
        # coins.sort(reverse=True)
        # minCompose = []
        # def change(remain:int, coinIndex:int, compose:[]):
        #     nonlocal minCompose
        #     if remain == 0:
        #         minCompose = [0]
        #     else:
        #         maxPiece = int(remain / coins[coinIndex])
        #         for count in range(maxPiece, -1, -1):
        #             nextRemain = remain - count * coins[coinIndex]
        #             nextCompose = compose + [count]
        #             nextCoinIndex = coinIndex + 1
        #             if nextRemain == 0:
        #                 if sum(nextCompose) < sum(minCompose) or len(minCompose) == 0:
        #                     minCompose = nextCompose
        #             elif nextRemain > 0 and (sum(nextCompose) < sum(minCompose) or len(minCompose) == 0):
        #                 if nextCoinIndex < len(coins):
        #                     change(nextRemain, nextCoinIndex, nextCompose)
        # change(amount, 0, [])
        # return -1 if len(minCompose) == 0 else sum(minCompose)

        # Solution 3 (remove record)
        coins.sort(reverse=True)
        minCompose = sys.maxsize
        def change(remain:int, coinIndex:int, compose:int):
            nonlocal minCompose
            if remain == 0:
                minCompose = 0
                return
            if coinIndex == len(coins):
                return
            if compose >= minCompose:
                return
            piece_max = int(remain / coins[coinIndex])
            piece_max = piece_max if piece_max < minCompose - compose else minCompose - compose
            for count in range(piece_max, -1, -1):
                nextCompose = compose + count
                nextRemain = remain - count * coins[coinIndex]
                if nextRemain == 0:
                    minCompose = nextCompose
                    break
                else:
                    change(nextRemain, coinIndex + 1, nextCompose)
        change(amount, 0, 0)
        return -1 if minCompose == sys.maxsize else minCompose
# print(Solution().coinChange([1, 2, 5], 11))
# print(Solution().coinChange([1, 2, 5], 70))
# print(Solution().coinChange([1], 0))
# print(Solution().coinChange([1], 1))
# print(Solution().coinChange([2], 3))
# print(Solution().coinChange([186,419,83,408], 6249))
# print(Solution().coinChange([3,7,405,436], 8839))
# print(Solution().coinChange([270,373,487,5,62], 8121))
# print(Solution().coinChange([227,99,328,299,42,322], 9847))
# print(Solution().coinChange([288,160,10,249,40,77,314,429], 9208))
