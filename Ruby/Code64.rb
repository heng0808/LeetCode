# @param {Integer[][]} grid
# @return {Integer}
def min_path_sum(grid)
    grid.each_index do |i|
        grid[i].each_index do |j|
            if i == 0 and j == 0
                next
            elsif i == 0
                grid[i][j] += grid[i][j - 1]
            elsif j == 0
                grid[i][j] += grid[i - 1][j]
            else
                grid[i][j] += [grid[i][j - 1], grid[i - 1][j]].min
            end
        end
    end
    grid[-1][-1]
end

puts min_path_sum [[1,3,1],[1,5,1],[4,2,1]]