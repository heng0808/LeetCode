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
        # total = []
        # for count in range(target + 1, 1, -1):
        #     first = (target - count * (count - 1) * 0.5) / count
        #     if first > 0 and first % 1 == 0:
        #         result = []
        #         first = int(first)
        #         for i in range(0, count):
        #             result.append(first + i)
        #         total.append(result)
        # return total
        
        # Solution 3
        total = []
        last = int(target / 2) if target % 2 == 0 else int((target + 1) / 2)
        left = 1
        right = 2
        while last > 1 and left != right and right <= last:
            result = sum(range(left, right + 1))
            if result == target:
                total.append(list(range(left, right + 1)))
                right = right + 1
            elif result < target:
                right = right + 1
            else:
                left = left + 1
        return total
Solution().findContinuousSequence(10)