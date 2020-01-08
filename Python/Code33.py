class Solution:
    def search(self, nums: [int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        min_index = -1
        while True:
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
        if target > nums[0] and target < nums[min_index - 1]:
            target_nums = nums[:min_index]
        else:
            target_nums = nums[min_index:]
        left = 0
        right = len(target_nums) - 1
        while True:
            mid = int((left + right) / 2)
            if target > target_nums[mid]:
                left = mid
            elif target < target_nums[mid]:
                right = mid
            else:
                return mid

print(Solution().search([9,0,1], 1))
# print(Solution().search([4,5,6,7,8,9,0,1,2], 7))