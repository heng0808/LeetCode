#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#
from typing import List
# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 单调队列
        # 对于里面的每个值，都是Push一遍Pop一遍
        ans = []
        queue = []
        for i in range(0, min(k, len(nums))):
            while len(queue) > 0 and queue[-1][-1] < nums[i]:
                queue.pop()
            queue.append((i, nums[i]))
        ans.append(queue[0][-1])
        for i in range(k, len(nums)):
            if i - k == queue[0][0]:
                queue.pop(0)
            while len(queue) > 0 and queue[-1][-1] < nums[i]:
                queue.pop()
            queue.append((i, nums[i]))
            ans.append(queue[0][-1])
        return ans
# @lc code=end
print(Solution().maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
# print(Solution().maxSlidingWindow([1, -1], 1))

