class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        arr = [[0 for i in range(0, n)] for j in range(0, m)]
        ans = 0
        def moveNext(i, j, step):
            nonlocal ans, arr
            if arr[i][j] == 0:
                row_sum = i // 100 + (i % 100) // 10 + (i % 10)
                col_sum = j // 100 + (j % 100) // 10 + (j % 10)
                if row_sum + col_sum <= k:
                    arr[i][j] = 1
                    if i != 0:
                        moveNext(i - 1, j, step + 1)
                    if i < m - 1:
                        moveNext(i + 1, j, step + 1)
                    if j != 0:
                        moveNext(i, j - 1, step + 1)
                    if j < n - 1:
                        moveNext(i, j + 1, step + 1)
                    arr[i][j] = 0
                else:
                    ans = max(ans, step - 1)
            else:
                ans = max(ans, step - 1)
        for i in range(0, m):
            for j in range(0, n):
                moveNext(i, j, 1)
        return ans

print(Solution().movingCount(16,8,4))

