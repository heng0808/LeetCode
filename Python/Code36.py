from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkBox(x:int, y:int):
            pass
        def checkRow(x:int, y:int):
            pass
        def checkCol(x:int, y:int):
            pass
        for x in range(0, len(board)):
            for y in range(0, len(board[x])):
                if checkBox(x, y) and checkRow(x, y) and checkCol(x, y):
                    continue
                else:
                    return False
        return True