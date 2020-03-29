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
        i = len(nums) - 2
        while i >= 0:
            if nums[i] < nums[i + 1]:
                # 找到了
                j = len(nums) - 1
                while j > i:
                    if nums[j] > nums[i]:
                        # 找到交换的了
                        temp = nums[j]
                        nums[j] = nums[i]
                        nums[i] = temp
                        for k in range(i + 1, len(nums)):
                            for l in range(k + 1, len(nums)):
                                if nums[k] > nums[l]:
                                    temp = nums[l]
                                    nums[l] = nums[k]
                                    nums[k] = temp
                        return
                    j = j - 1
            i = i - 1
        nums.sort(reverse=False)


# nums = [1, 2, 3]
# nums = [1, 1, 5]
nums = [1, 3, 2]
Solution().nextPermutation(nums)
print(nums)