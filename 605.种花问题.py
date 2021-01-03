#
# @lc app=leetcode.cn id=605 lang=python3
#
# [605] 种花问题
#
from typing import List
# @lc code=start
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) < 2 * n - 1:
            return False
        if n == 0:
            return True
        # 满足种花条件的区间个数
        count = n
        for i in range(0, len(flowerbed)):
            if flowerbed[i] == 0:
                left_ok = False
                right_ok = False
                if i == 0:
                    left_ok = True
                elif flowerbed[i-1] == 0:
                    left_ok = True
                if i == len(flowerbed) - 1:
                    right_ok = True
                elif flowerbed[i+1] == 0:
                    right_ok = True
                if left_ok and right_ok:
                    flowerbed[i] = 1
                    count -= 1
                if count == 0:
                    return True

        count = n
        for i in range(len(flowerbed) - 1, -1, -1):
            if flowerbed[i] == 0:
                left_ok = False
                right_ok = False
                if i == 0:
                    left_ok = True
                elif flowerbed[i-1] == 0:
                    left_ok = True
                if i == len(flowerbed) - 1:
                    right_ok = True
                elif flowerbed[i+1] == 0:
                    right_ok = True
                if left_ok and right_ok:
                    flowerbed[i] = 1
                    count -= 1
                if count == 0:
                    return True
        return False
# @lc code=end

print(Solution().canPlaceFlowers([1,0,0,0,0,1], 2))