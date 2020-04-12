#
# @lc app=leetcode.cn id=81 lang=python3
#
# [81] 搜索旋转排序数组 II
#
from typing import List
# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if len(nums) == 0:
            return False
        if len(nums) <= 2:
            return True if nums[0] == target or nums[-1] == target else False
        left, right = 0, len(nums) - 1
        while left <= right:
            if right - left <= 1:
                if nums[left] == target or nums[right] == target:
                    return True
                break
            if nums[left] == target or nums[right] == target:
                return True
            elif nums[left] == nums[right]:
                left += 1
            else:
                mid = (left + right) // 2
                # 不是左递增就是右递增
                if nums[mid] >= nums[left]:
                    # 左连续
                    # 不在左递增就在对面
                    if target >= nums[left] and target <= nums[mid]:
                        right = mid
                    else:
                        left = mid
                else:
                    # 右递增
                    # 不在右递增就在对面    
                    if target >= nums[mid] and target <= nums[right]:
                        left = mid
                    else:
                        right = mid
        return False
# @lc code=end
print(Solution().search([2,5,6,0,0,1,2], 0))
print(Solution().search([2,1,2], 2))
print(Solution().search([4,5,6,7,0,1,2], 3))