#
# @lc app=leetcode.cn id=72 lang=python3
#
# [72] 编辑距离
#
# dp[i][j]代表长度为i的字符串变为长度为j的字符串的操作次数
# word[i] == word[j] => dp[i][j] == dp[i-1][j+1]
# word[i] != word[j] => dp[i][j] = 1 + min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j])
# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = []
        for i in range(0, len(word1) + 1):
            dp.append([])
            for j in range(0, len(word2) + 1):
                dp[-1].append(0)

        for i in range(0, len(word1) + 1):
            for j in range(0, len(word2) + 1):
                if i == 0 and j == 0:
                    # 空字符串到空字符串
                    dp[i][j] = 0
                elif i == 0:
                    # 空字符串到任意字符串
                    dp[i][j] = 1 + dp[i][j-1]
                elif j == 0:
                    # 任意字符串到空字符串
                    dp[i][j] = 1 + dp[i-1][j]
                else:
                    if word1[i-1] == word2[j-1]:
                        dp[i][j] = dp[i-1][j-1]
                    else:
                        dp[i][j] = 1 + min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j])

        return dp[-1][-1]

# @lc code=end
print(Solution().minDistance("horse", "ros"))
print(Solution().minDistance("", "ros"))
print(Solution().minDistance("horse", ""))
