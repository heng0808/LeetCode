# @Time    : 2019-07-21 17:08
# @Author  : 张恒
# @File    : Code11.py
# @Software: PyCharm


class Solution:
    def maxArea(self, height: [int]):
        left = 0
        right = len(height) - 1
        max_area = (right - left) * min(height[left], height[right])
        while left != right:
            left_value = height[left]
            right_value = height[right]
            if left_value < right_value:
                left = left + 1
            else:
                right = right - 1
            max_area = max(max_area, (right - left) * min(height[left], height[right]))
        return max_area
print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))