#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#
from typing import List
# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def sort(item):
            return item[0]
        intervals.sort(key=sort)
        ans = []
        for item in intervals:
            if len(ans) == 0:
                ans.append(item)
            else:
                if ans[-1][-1] >= item[0]:
                    ans[-1][-1] = max(ans[-1][-1], item[1])
                else:
                    ans.append(item)
        return ans
# @lc code=end
print(Solution().merge([[1,3],[2,6],[8,10],[15,18]]))

