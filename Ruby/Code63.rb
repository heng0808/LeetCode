# @param {Integer[][]} obstacle_grid
# @return {Integer}
def unique_paths_with_obstacles(obstacle_grid)
    obstacle_grid.each_index do |i|
        obstacle_grid[i].each_index do |j|
            if obstacle_grid[i][j] == 1
                next
            elsif i == 0 and j == 0
                obstacle_grid[i][j] = -1
            elsif i == 0
                left = obstacle_grid[i][j-1] == 1 ? 0 : obstacle_grid[i][j-1]
                obstacle_grid[i][j] = 0 + left
            elsif j == 0                
                up = obstacle_grid[i-1][j] == 1 ? 0 : obstacle_grid[i-1][j]
                obstacle_grid[i][j] = up + 0
            else
                up = obstacle_grid[i-1][j] == 1 ? 0 : obstacle_grid[i-1][j]
                left = obstacle_grid[i][j-1] == 1 ? 0 : obstacle_grid[i][j-1]
                obstacle_grid[i][j] = up + left
            end
        end
    end
    if obstacle_grid[-1][-1] == 1
        0
    else
        -obstacle_grid[-1][-1]
    end
end

puts unique_paths_with_obstacles [[0,0,0],[0,1,0],[0,0,0]]