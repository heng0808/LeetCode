from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkRow(x: int, y: int, value):
            for index in range(0, 9):
                if index != y and board[x][index] == board[x][y]:
                    return False
            return True

        def checkCol(x: int, y: int, value):
            for index in range(0, 9):
                if index != x and board[index][y] == board[x][y]:
                    return False
            return True

        def checkBox(x: int, y: int, value):
            for row_index in range(int(x / 3) * 3, int(x / 3) * 3 + 3):
                for col_index in range(int(y / 3) * 3, int(y / 3) * 3 + 3):
                    if row_index != x and col_index != y and board[row_index][col_index] == board[x][y]:
                        return False
            return True

        for x in range(0, len(board)):
            for y in range(0, len(board[x])):
                if board[x][y] == '.':
                    continue
                elif checkBox(x, y, board[x][y]) and checkRow(x, y, board[x][y]) and checkCol(x, y, board[x][y]):
                    continue
                else:
                    return False
        return True

# print(Solution().isValidSudoku([
#   ["5","3",".",".","7",".",".",".","."],
#   ["6",".",".","1","9","5",".",".","."],
#   [".","9","8",".",".",".",".","6","."],
#   ["8",".",".",".","6",".",".",".","3"],
#   ["4",".",".","8",".","3",".",".","1"],
#   ["7",".",".",".","2",".",".",".","6"],
#   [".","6",".",".",".",".","2","8","."],
#   [".",".",".","4","1","9",".",".","5"],
#   [".",".",".",".","8",".",".","7","9"]
# ]))

print(Solution().isValidSudoku([
 ["8","3",".",".","7",".",".",".","."],
 ["6",".",".","1","9","5",".",".","."],
 [".","9","8",".",".",".",".","6","."],
 ["8",".",".",".","6",".",".",".","3"],
 ["4",".",".","8",".","3",".",".","1"],
 ["7",".",".",".","2",".",".",".","6"],
 [".","6",".",".",".",".","2","8","."],
 [".",".",".","4","1","9",".",".","5"],
 [".",".",".",".","8",".",".","7","9"]
]));

