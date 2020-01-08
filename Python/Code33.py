class Solution:
    def search(self, nums: [int], target: int) -> int:
        if len(nums) == 0:
            return -1
        elif len(nums) == 1:
            return 0 if target == nums[0] else -1
        elif len(nums) == 2:
            return 0 if target == nums[0] else 1 if target == nums[1] else -1
        left = 0
        right = len(nums) - 1
        min_index = -1
        while True:
            if right - left == 1:
                # 就两个
                min_index = left if nums[left] < nums[right] else right
                break
            else:
                mid = int((left + right) / 2)
                if nums[mid] < nums[mid - 1] and nums[mid] < nums[mid + 1]:
                    min_index = mid
                    break
                if nums[mid] > nums[right]:
                    # 0 在右边
                    left = mid
                else:
                    # 0 在左边
                    right = mid

        if nums[min_index] <= target <= nums[len(nums) - 1]:
            left = min_index
            right = len(nums) - 1
        else:
            left = 0
            right = min_index - 1

        while left <= right:
            if left == right:
                return left if target == nums[left] else -1
            elif right - left == 1:
                # 就两个
                return left if target == nums[left] else right if target == nums[right] else -1
            else:
                mid = int((left + right) / 2)
                if target > nums[mid]:
                    left = mid
                elif target < nums[mid]:
                    right = mid
                else:
                    return mid
        return -1

# print(Solution().search([1], 0))
# print(Solution().search([9,0,1], 1))
print(Solution().search([3,5,1], 1))
# print(Solution().search([5, 1, 3], 0))
# print(Solution().search([4,5,6,7,8,9,0,1,2], 7))