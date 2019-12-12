class Solution:
    def removeElement(self, nums: [int], val: int) -> int:
        i = -1
        for j in range(0, len(nums)):
            if nums[j] != val:
                nums[i+1] = nums[j]
                i += 1
        return i+1
print(Solution().removeElement([], 2))