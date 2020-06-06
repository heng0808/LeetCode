from typing import List
class Solution:
    # 有序数组，可用前后双指针
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i, j = 0, len(nums) - 1
        while i < j:
            res = nums[i] + nums[j]
            if res == target:
                return [nums[i], nums[j]]
            elif res < target:
                i += 1
            elif res > target:
                j -= 1

print(Solution().twoSum([2,7,11,15], 22))
