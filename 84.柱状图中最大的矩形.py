#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#
from typing import List
from sys import maxsize
# @lc code=start
class Solution:
    # 单调栈
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        stack = []
        heights.append(0)
        for index in range(0, len(heights)):
            if len(stack) > 0 and heights[stack[-1]] >= heights[index]:
                # 减小了 计算前面最大
                while len(stack) > 0 and heights[stack[-1]] >= heights[index]:
                    left_index = stack.pop()
                    stack_length = len(stack)
                    if stack_length == 1:
                        if heights[-1] == 0:
                            ans = max(ans, (index - (stack[-1] + 1)) * heights[left_index])
                        else:
                            ans = max(ans, (index - left_index + (left_index - stack[-1] - 1)) * heights[left_index])
                    elif stack_length == 0:
                        ans = max(ans, index * heights[left_index])
                    else:
                        ans = max(ans, (index - left_index + (left_index - stack[-1] - 1)) * heights[left_index])
            stack.append(index)
        return ans
    # 分治
    # def largestRectangleArea(self, heights: List[int]) -> int:
    #     ans = 0
    #     def caculateArea(start=0, end=len(heights) - 1):
    #         if end < start:
    #             return
    #         minHeight = maxsize
    #         minIndex = -1
    #         for index in range(start, end + 1):
    #             if heights[index] < minHeight:
    #                 minHeight = heights[index]
    #                 minIndex = index
    #         nonlocal ans
    #         if minIndex != -1:
    #             ans = max((end - start + 1) * minHeight, ans)
    #             caculateArea(start, minIndex - 1)
    #             caculateArea(minIndex + 1, end)
    #     caculateArea()
    #     return ans

    # 优化暴力
    # def largestRectangleArea(self, heights: List[int]) -> int:
    #     if len(heights) == 0:
    #         return 0
    #     ruler = 1
    #     ans = 0
    #     while len(heights) > 0:
    #         stack = []
    #         nextRuler = maxsize
    #         nextHeights = []
    #         for height in heights:
    #             if height >= ruler:
    #                 stack.append(height)
    #             else:
    #                 result = len(stack) * ruler
    #                 if result > ans:
    #                     ans = result
    #                     nextHeights = stack[0:]
    #                 stack.clear() 
    #             if height > ruler and height < nextRuler:
    #                 nextRuler = height
    #         result = len(stack) * ruler
    #         if result > ans:
    #             ans = result
    #             nextHeights = stack[0:]
    #         if nextRuler != 0: 
    #             ruler = nextRuler
    #         else:
    #             ruler = ruler + 1
    #         heights = nextHeights
    #     return ans
# @lc code=end
print(Solution().largestRectangleArea([5,5,1,7,1,1,5,2,7,6]))
# print(Solution().largestRectangleArea([3,6,5,7,4,8,1,0]))
# print(Solution().largestRectangleArea([4,2,0,3,2,5]))
# print(Solution().largestRectangleArea([2,0,5,6,2,3]))
# print(Solution().largestRectangleArea([5,4,1,2]))
# print(Solution().largestRectangleArea([1]))
# print(Solution().largestRectangleArea([0,0,0,0,0,0,0,0,2147483647]))
# print(Solution().largestRectangleArea([0,1,2,3,4,5]))
# print(Solution().largestRectangleArea([1,1,1,1,1,1,1]))