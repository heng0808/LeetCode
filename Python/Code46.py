class Solution:
    def permute(self, nums: [int]) -> [[int]]:
        sequences = []

        def permutation(sequence: [int], nums: [int]):
            if len(nums) == 0:
                sequences.append(sequence)
            for index in range(0, len(nums)):
                temp = sequence[:]
                temp.append(nums[index])
                temp_nums = nums[:]
                del temp_nums[index]
                permutation(temp, temp_nums)

        permutation([], nums)
        return sequences


print(Solution().permute([1, 2, 3]))
