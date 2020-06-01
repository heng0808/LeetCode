from typing import List
class Solution:
    # 记录次数
    def majorityElement(self, nums: List[int]) -> int:
        currentNum, currentCount= nums[0], 1
        for num in nums[1:]:
            if currentCount == 0:
                currentNum = num
                currentCount = 1
            else:
                if num == currentNum:
                    currentCount += 1
                else:
                    currentCount -= 1
        return currentNum