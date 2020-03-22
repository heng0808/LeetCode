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
        
# print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(Solution().maxSubArray([-2,-1]))
# print(Solution().maxSubArray([1]))