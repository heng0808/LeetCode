class Solution:
    def totalNQueens(self, n: int) -> int:
        ans = 0
        def nextPostion(index: int, permutations:[]):
            if index == n:
                nonlocal ans
                ans = ans + 1
                
            for i in range(0, n):
                if i in permutations:
                    continue
                illegal = False
                for j in range(len(permutations) - 1, -1, -1):
                    if abs(permutations[j] - i) == len(permutations) - j:
                        illegal = True
                        break
                if illegal == False:
                    permutations.append(i)
                    nextPostion(index + 1, permutations)
                    permutations.pop()
        nextPostion(0, [])
        return ans

print(Solution().totalNQueens(4))