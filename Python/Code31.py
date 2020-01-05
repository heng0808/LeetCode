class Solution:
    def nextPermutation(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return
        elif len(nums) == 2:
            temp = nums[1]
            nums[1] = nums[0]
            nums[0] = temp
            return
        min_left = len(nums) - 1
        while min_left > 0:
            min_left = min_left - 1
            if nums[min_left] < nums[min_left + 1]:
                break
        if min_left > 0:
            max_right = min_left + 1
            while max_right < len(nums):
                if nums[max_right] < nums[min_left]:
                    max_right = max_right - 1
                    break
                max_right = max_right + 1
        else:
            nums.sort()

# nums = [1, 2, 3]
# nums = [1, 1, 5]
nums = [1, 2, 1]
Solution().nextPermutation(nums)
print(nums)