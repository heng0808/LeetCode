class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index1 in range(0, len(nums) - 1):
            num_left = target - nums[index1]
            nums_left = nums[index1 + 1:]
            try:
                return [index1, nums_left.index(num_left) + index1 + 1]
            except BaseException as error:
                continue
        return []
if __name__ == '__main__':
    reulst = Solution().twoSum([0,4,3,0], 0)
    pass