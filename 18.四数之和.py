class Solution:
    def fourSum(self, nums: [int], target: int) -> [[int]]:
        nums = sorted(nums)
        if len(nums) < 4:
            return []
        if nums[0] == nums[len(nums) - 1]:
            if 4 * nums[0] == target:
                return [[nums[0],nums[0],nums[0],nums[0]]]
            return []
        resultSet = set()
        for i in range(0, len(nums)):
            for j in range(i + 1, len((nums))):
                left = j + 1
                right = len(nums) - 1
                while left < right:
                    num1 = nums[i]
                    num2 = nums[j]
                    num3 = nums[left]
                    num4 = nums[right]
                    sum = num1 + num2 + num3 + num4
                    if sum > target:
                        right = right - 1
                    elif sum < target:
                        left = left + 1
                    else:
                        resultSet.add(str([num1, num2, num3, num4]))
                        left = left + 1
                        right = right - 1
        resultList = []
        for resultStr in resultSet:
            resultList.append(eval(resultStr))
        return resultList

# print(Solution().fourSum([1, 0, -1, 0, -2, 2], 0))
print(Solution().fourSum([0,0,0,0], 0))
