from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return 0
        left = 0
        right = len(nums) - 1
        while left <= right:
            if right - left <= 1:
                if nums[right] == target:
                    return right
                elif nums[left] == target:
                    return left
                else:
                    if left - right == 0:
                        if nums[left] < target:
                            return left + 1
                        else:
                            return left
                    else:
                        if target < nums[left]:
                            return left
                        elif target > nums[right]:
                            return right + 1
                        else:
                            return right
            else:
                mid = int((left + right) * 0.5)
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid
        return 0 if nums[0] > target else len(nums) - 1

print(Solution().searchInsert([1,3,5,6], 5))
print(Solution().searchInsert([1,3,5,6], 2))
print(Solution().searchInsert([1,3,5,6], 7))
print(Solution().searchInsert([1,3,5,6], 0))
print(Solution().searchInsert([1,3,5], 4))
print(Solution().searchInsert([3,5,7,9,10], 8))