#
# @lc app=leetcode.cn id=118 lang=ruby
#
# [118] 杨辉三角
#

# @lc code=start
# @param {Integer} num_rows
# @return {Integer[][]}
def generate(num_rows)
    ans = []
    (0...num_rows).each do |value|
        row = []
        (0..value).each do |index|
            if index == 0 || index == value
                row << 1
            else
                row << (ans[-1][index-1] + ans[-1][index])
            end
        end
        ans << row
    end
    ans
end
# @lc code=end

print generate 5

