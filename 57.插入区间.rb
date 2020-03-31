# 给出一个无重叠的 ，按照区间起始端点排序的区间列表。
# 在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。
# 示例:
# 输入: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# 输出: [[1,2],[3,10],[12,16]]
# 解释: 这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。

# @param {Integer[][]} intervals
# @param {Integer[]} new_interval
# @return {Integer[][]}
def insert(intervals, new_interval)
    if intervals.length == 0
        if new_interval.length == 0
            return []
        else
            return [new_interval] 
        end
    end
    left = 0
    mixed = false
    while left < intervals.length
        interval = intervals[left]
        if left == 0 and new_interval[-1] < interval[0]
            break
        elsif mixed == false and new_interval[-1] < interval[0]
            break
        elsif [interval[0], new_interval[0]].max <= [interval[1], new_interval[1]].min
            intervals.delete_at left
            mixed = true
            new_interval[0] = [interval[0], new_interval[0]].min
            new_interval[1] = [interval[1], new_interval[1]].max
        elsif mixed == true
            break
        else
            left = left + 1
        end
    end

    if left < intervals.length
        intervals.insert left, new_interval
    else
        intervals.push new_interval
    end
    return intervals
end

# print insert [[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]
# print insert [[1,3],[6,9]], [2,5]
# print insert [[1,3]], [2,5]
# print insert [[1,5]],[0,0]
# print insert [[1,5]],[6,9]
print insert [[3,5],[12,15]], [6,6]
