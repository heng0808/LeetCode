from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        return self.function2(nums)

    # 本身作为哈希表
    def function2(self, nums) -> int:
        # 3 应该放在索引为 2 的地方
        # 4 应该放在索引为 3 的地方
        def __swap(index1, index2):
            nums[index1], nums[index2] = nums[index2], nums[index1]
        size = len(nums)
        for i in range(size):
            # 先判断这个数字是不是索引，然后判断这个数字是不是放在了正确的地方
            while 1 <= nums[i] <= size and nums[i] != nums[nums[i] - 1]:
                __swap(i, nums[i] - 1)

        for i in range(size):
            if i + 1 != nums[i]:
                return i + 1

        return size + 1

    # 额外的哈希表
    def function1(self, nums) -> int:
        compare_nums = list(range(1, len(nums) + 1))
        for num in nums:
            if 1 <= num <= len(nums):
                compare_nums[num - 1] = None
        for compare_num in compare_nums:
            if compare_num is not None:
                return compare_num
        return 1 if len(nums) == 0 else len(compare_nums) + 1

      

# print(Solution().firstMissingPositive([7,8,9,11,12]))
print(Solution().firstMissingPositive([3, 4, -1, 1]))
# print(Solution().firstMissingPositive([1,2,0]))