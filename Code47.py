from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        sequences = []
        sequenceIndexs = []
        def permute():
            if len(sequences) == 0:
                return
            # 没什么可以选择的了
            if len(sequenceIndexs) == len(nums):
                sequence = []
                for i in sequenceIndexs:
                    sequence.append(nums[i])
                sequences.append(sequence)
                return
            # 还有可以选择的
            this_level_nums = []
            for i in range(0, len(nums)):
                if i in sequenceIndexs:
                    continue
                elif nums[i] in this_level_nums:
                    continue
                else:
                    this_level_nums.append(nums[i])
                    sequenceIndexs.append(i)
                    permute()
                    sequenceIndexs.pop()

        permute()
        return sequences

print(Solution().permuteUnique([]))