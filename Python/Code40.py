from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if len(candidates) == 0:
            return []
        total = []
        candidates.sort()
        map = {}
        def subtractionAlgorithm(begin:int, divisors: [int], remainder):
            if begin < len(candidates):
                for index in range(begin, len(candidates)):
                    num = candidates[index]
                    result = remainder - num
                    if result == 0:
                        if map.get(str(divisors + [num])) is None:
                            total.append(divisors + [num])
                        map.setdefault(str(divisors + [num]), "1")
                    elif result >= candidates[0]:
                        next_divisors = divisors + [num]
                        subtractionAlgorithm(index + 1, next_divisors, result)

        subtractionAlgorithm(0, [], target)
        return total

print(Solution().combinationSum2([10,1,2,7,6,1,5], 8))