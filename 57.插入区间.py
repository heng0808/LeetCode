#
# @lc app=leetcode.cn id=57 lang=python3
#
# [57] 插入区间
#
from typing import List
# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        arr = []
        while len(intervals) > 0:
            interval = intervals.pop(0)
            if interval[0] > newInterval[1]:
                arr = arr + [newInterval] + [interval] +intervals
                newInterval = []
                break
            elif newInterval[0] > interval[1]:
                arr.append(interval)
            else:
                newInterval = [min(interval[0], newInterval[0]), max(interval[1], newInterval[1])]
        if len(newInterval) > 0:
            arr.append(newInterval)
        return arr
# @lc code=end
print(Solution().insert([[1,5]], [6,8]))
print(Solution().insert([[1,3],[6,9]], [2,5]))
print(Solution().insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))
