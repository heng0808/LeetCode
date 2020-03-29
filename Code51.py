from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        allPermutations = []
        def nextPostion(index: int, permutations:[]):
            if index == n:
                postions = []
                for i in permutations:
                    row = ''
                    for j in range(0, n):
                        row = row + ('.' if j != i else 'Q')
                    postions.append(row)
                allPermutations.append(postions)
                
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
        return allPermutations

print(Solution().solveNQueens(5))