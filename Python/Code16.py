class Solution:
    def threeSumClosest(self, nums: [int], target: int) -> int:
        nums = sorted(nums)
        if len(nums) < 3:
            return []
        if nums[0] == nums[len(nums) - 1]:
            return nums[0] + nums[1] + nums[2]
        closeNums = []
        closeSum = None
        for index in range(0, len(nums)):
            left = index + 1
            right = len(nums) - 1
            while left < right:
                num1 = nums[index]
                num2 = nums[left]
                num3 = nums[right]
                sum = num1 + num2 + num3

                if closeSum == None:
                    closeSum = sum
                    closeNums = [num1, num2, num3]

                if abs(sum - target) < abs(closeSum - target):
                    closeSum = sum
                    closeNums = [num1, num2, num3]

                if sum > target:
                    right = right - 1
                elif sum < target:
                    left = left + 1
                else:
                    closeSum = sum
                    closeNums = [num1, num2, num3]
                    break

        return closeSum

# print(Solution().threeSumClosest([-1,2,1,-4], 100))
# print(Solution().threeSumClosest([0,2,1,-3], 1))
# print(Solution().threeSumClosest([1,2,4,8,16,32,64,128], 82));
# print(Solution().threeSumClosest([4,0,5,-5,3,3,0,-4,-5], -2))
print(Solution().threeSumClosest([-55,-24,-18,-11,-7,-3,4,5,6,9,11,23,33], 0))


