#
# @lc app=leetcode.cn id=860 lang=python3
#
# [860] 柠檬水找零
#
from typing import List
# @lc code=start
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count_5 = 0
        count_10 = 0
        for bill in bills:
            if bill == 20:
                count_10 -= 1
                if count_10 < 0:
                    count_10 = 0
                    count_5 -= 2
                count_5 -= 1
            if bill == 10:
                count_5 -= 1
            if count_5 < 0 or count_10 < 0:
                return False
            if bill == 10:
                count_10 += 1
            if bill == 5:
                count_5 += 1
        return True        
# @lc code=end
print(Solution().lemonadeChange([5,5,10,20,5,5,5,5,5,5,5,5,5,10,5,5,20,5,20,5]))