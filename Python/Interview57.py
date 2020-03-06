class Solution:
    def findContinuousSequence(self, target: int) -> [[int]]:
        # Solution 1
        # total = []
        # for first in range(1, int(target / 2) + 1):
        #     d = pow(pow(2*first - 1, 2) + 8*target, 0.5)
        #     n = (-(2 * first - 1) + d) / 2
        #     if n % 1 == 0:
        #         result = []
        #         for i in range(0, int(n)):
        #             result.append(first + i)
        #         total.append(result)
        # return total

        # Solution 2
        total = []
        for count in range(target + 1, 1, -1):
            first = (target - count * (count - 1) * 0.5) / count
            if first > 0 and first % 1 == 0:
                result = []
                first = int(first)
                for i in range(0, count):
                    result.append(first + i)
                total.append(result)
        return total
Solution().findContinuousSequence(9)