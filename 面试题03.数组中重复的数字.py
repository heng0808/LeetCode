from typing import List
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        table = {}
        for num in nums:
            if num in table:
                return num
            else:
                table[num] = 1
        return 0

