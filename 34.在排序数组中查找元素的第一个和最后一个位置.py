from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findLeft() -> int:
            left = 0
            right = len(nums) - 1
            while left <= right:
                if right - left <= 1:
                    return left if nums[left] == target else right if nums[right] == target else -1
                else:
                    mid = int((left + right) * 0.5)
                    if nums[mid] < target:
                        left = mid
                    elif nums[mid] > target:
                        right = mid
                    else:
                        right = mid
            return -1
        def findRight() -> int:
            left = 0
            right = len(nums) - 1
            while left <= right:
                if right - left <= 1:
                    return right if nums[right] == target else left if nums[left] == target else -1
                else:
                    mid = int((left + right) * 0.5)
                    if nums[mid] < target:
                        left = mid
                    elif nums[mid] > target:
                        right = mid
                    else:
                        left = mid
            return -1
        return [findLeft(), findRight()]

Solution().searchRange([1,2,3,4,5,6], 5)
# Solution().searchRange([8, 8, 8], 7)
# Solution().searchRange([5,7,7,8,8,10], 8)