from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        compare_nums = list(range(1, len(nums) + 1))
        for num in nums:
            if 1 <= num <= len(nums):
                compare_nums[num - 1] = None
        for compare_num in compare_nums:
            if compare_num is not None:
                return compare_num
        return 1 if len(nums) == 0 else len(compare_nums) + 1

# print(Solution().firstMissingPositive([7,8,9,11,12]))
# print(Solution().firstMissingPositive([3, 4, -1, 1]))
print(Solution().firstMissingPositive([1,2,0]))