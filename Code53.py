# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
# 示例：
# 输入: [-2,1,-3,4,-1,2,1,-5,4],
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
from typing import List
from sys import maxsize

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        ans = -maxsize
        # left->right
        left = 0
        right = left + 1
        result = nums[left]
        while right < len(nums):
            if result < 0 and nums[right] > result:
                result = nums[right]
                left = right
            else:
                result = result + nums[right]
            ans = ans if ans > result else result
            right = right + 1
        
        # right->left
        right = len(nums) -1
        left = right - 1
        result = nums[right]
        while left >= 0:
            if result < 0 and nums[left] > result:
                result = nums[left]
                right = left
            else:
                result = result + nums[left]
            ans = ans if ans > result else result
            left = left - 1
        
        return ans

    # def maxSubArray(self, nums: List[int]) -> int:
    #     # 最大序列要么再左边，要么在右边，要么在中间，子序列也是一样的
    #     if len(nums) == 1:
    #         return nums[0]
    #     else:
    #         mid = int(len(nums) / 2)
    #         mid_ml = -maxsize
    #         temp = 0
    #         for i in range(mid - 1, -1, -1):
    #             temp = temp + nums[i]
    #             mid_ml = max(mid_ml, temp)
            
    #         mid_mr = -maxsize
    #         temp = 0
    #         for i in range(mid, len(nums)):
    #             temp = temp + nums[i]
    #             mid_mr = max(mid_mr, temp)
    #     return max(self.maxSubArray(nums[0:mid]), self.maxSubArray(nums[mid:len(nums)]), mid_ml + mid_mr)
print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(Solution().maxSubArray([-2,-1]))
print(Solution().maxSubArray([1]))