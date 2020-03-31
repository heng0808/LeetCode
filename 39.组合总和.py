from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if len(candidates) == 0:
            return []
        total = []
        candidates.sort()
        def subtractionAlgorithm(divisors:[int], remainder):
            for num in candidates:
                if len(divisors) == 0 or num >= divisors[-1]:
                    result = remainder - num
                    if result == 0:
                        total.append(divisors + [num])
                    elif result >= candidates[0]:
                        next_divisors = divisors + [num]
                        subtractionAlgorithm(next_divisors, result)

        subtractionAlgorithm([], target)
        return total

print(Solution().combinationSum([2,3,5], 8))