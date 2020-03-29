# @param {Integer} m
# @param {Integer} n
# @return {Integer}
def unique_paths(m, n)
    dp = Array.new(m){ Array.new(n) }
    for i in 0...m
        for j in 0...n
            if i == 0 and j == 0
                dp[i][j] = 1
            elsif i == 0
                dp[i][j] = 0 + dp[i][j-1]
            elsif j == 0
                dp[i][j] = dp[i-1][j] + 0
            else
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
            end
        end
    end
    return dp[m-1][n-1]
end

# def unique_paths(m, n)
#     if m == 1 || n == 1
#         return 1
#     end
#     n = (m - 1 + n - 1)
#     m = m - 1
#     ans = (1..n).reduce(:*) / ((1..m).reduce(:*) * (1..(n-m)).reduce(:*))
# end

puts unique_paths(7, 3)