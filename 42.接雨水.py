from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        left = 0
        right = len(height) - 1
        maxLeft = 0
        maxRight = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] < maxLeft:
                    ans = ans + (maxLeft - height[left])
                else:
                    maxLeft = height[left]
                left = left + 1
            else:
                if height[right] < maxRight:
                    ans = ans + (maxRight - height[right])
                else:
                    maxRight = height[right]
                right = right - 1
        return ans

    def trap1(self, height: List[int]) -> int:
        ans = 0
        # left = 0
        # right = len(height) - 1
        # maxLeft = 0
        # maxRight = 0
        # while left < right:
        #     if height[left] < height[right]:
        #         if height[left] < maxLeft:
        #             ans = ans + (maxLeft - height[left])
        #         else:
        #             maxLeft = height[left]
        #         left = left + 1
        #     else:
        #         if height[right] < maxRight:
        #             ans = ans + (maxRight - height[right])
        #         else:
        #             maxRight = height[right]
        #         right = right - 1
        return ans
print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))