# 给定一个正整数 n，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。
# 示例:
# 输入: 3
# 输出:
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]

# @param {Integer} n
# @return {Integer[][]}
def generate_matrix(n)
    matrix = [[0] * n] * n
    arr = Array.new(n * n) do |index|
        index + 1
    end
    
    return matrix
end

print generate_matrix 3