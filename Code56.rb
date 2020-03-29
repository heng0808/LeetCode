# 给出一个区间的集合，请合并所有重叠的区间。
# 示例:
# 输入: [[1,3],[2,6],[8,10],[15,18]]
# 输出: [[1,6],[8,10],[15,18]]
# 解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].

# @param {Integer[][]} intervals
# @return {Integer[][]}
def merge(intervals)
    ans = []
    until intervals.empty? do
        interval = intervals.pop
        if ans.empty?
            ans.push interval
        else
            while true
                mixed = false
                ans.each do |region|
                    if [region[0], interval[0]].max <= [region[1], interval[1]].min
                        ans.delete region
                        interval[0] = [region[0], interval[0]].min
                        interval[1] = [region[1], interval[1]].max
                        mixed = true
                        break
                    end
                end
                if mixed == false
                    break
                end
            end
            ans.push interval
        end
    end
    return ans
end

# print merge [[2,3],[4,5],[6,7],[8,9],[1,10]]
# print merge [[1,3],[2,6],[8,10],[15,18]]
# print merge [[1,4],[0,2],[3,5]]
# print merge [[1,4],[4,5]]
# print merge [[1,4],[0,4]]
print merge []