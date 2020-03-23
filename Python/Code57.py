# 给出一个无重叠的 ，按照区间起始端点排序的区间列表。
# 在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。
# 示例:
# 输入: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# 输出: [[1,2],[3,10],[12,16]]
# 解释: 这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。

from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            if len(newInterval) == 0:
                return []
            else:
                return [newInterval]
        
        left = 0
        mixed = False
        while left < len(intervals):
            interval = intervals[left]
            if (left == 0 or mixed == False) and newInterval[-1] < interval[0]:
                break
            elif max(interval[0], newInterval[0]) <= min(interval[1], newInterval[1]):
                intervals.pop(left)
                mixed = True
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(interval[1], newInterval[1])
            elif mixed == True:
                break
            else:
                left = left + 1

        if left < len(intervals):
            intervals.insert(left, newInterval)
        else:
            intervals.append(newInterval)

        return intervals

print(Solution().insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))
print(Solution().insert([[1,3],[6,9]], [2,5]))
print(Solution().insert([[1,3]], [2,5]))
print(Solution().insert([[1,5]],[0,0]))
print(Solution().insert([[1,5]],[6,9]))
print(Solution().insert([[3,5],[12,15]], [6,6]))