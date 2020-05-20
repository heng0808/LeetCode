#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: [int], target: int) -> int:
        nums = sorted(nums)
        closeSum = None
        for i in range(0, len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                tempSum = nums[i] + nums[left] + nums[right]
                if closeSum == None:
                    closeSum = tempSum
                else:
                    if abs(tempSum - target) < abs(closeSum - target):
                        closeSum = tempSum
                if tempSum > target:
                    right = right - 1
                else:
                    left = left + 1
        return closeSum
# @lc code=end
print(Solution().threeSumClosest([0,2,1,-3], 1))
