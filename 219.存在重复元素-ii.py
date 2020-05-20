#
# @lc app=leetcode.cn id=219 lang=python3
#
# [219] 存在重复元素 II
#
from typing import List
# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        table = {}
        for i in range(0, len(nums)):
            num = nums[i]
            if num in table:
                if i - table[num] <= k:
                    return True
                else:
                    table[num] = i
            else:
                table[num] = i
        return False
# @lc code=end
print(Solution().containsNearbyDuplicate([1,2,3,1,2,3], 2))
