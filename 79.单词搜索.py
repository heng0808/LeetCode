#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#
from typing import List
# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(board) == 0 or len(board[0]) == 0:
            return False
        def find(i:int, j:int, index:int):
            if i < 0:
                return False
            if j < 0:
                return False
            if i >= len(board):
                return False
            if j >= len(board[i]):
                return False
            if board[i][j] != '' and board[i][j] == word[index]:
                if index == len(word) - 1:
                    return True
                character = board[i][j]
                board[i][j] = ''
                if find(i + 1, j, index + 1):
                    return True
                if find(i - 1, j, index + 1):
                    return True
                if find(i, j + 1, index + 1):
                    return True
                if find(i, j - 1, index + 1):
                    return True
                board[i][j] = character
            return False
        for i in range(0, len(board)):
            for j in range(0, len(board[i])):
                if find(i, j, 0):
                    return True
        return False
# @lc code=end
# [['A','B','C','E'],
#  ['S','F','C','S'],
#  ['A','D','E','E']]
print(Solution().exist(board=[['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], word="ABCCED"))
print(Solution().exist(board=[['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], word="SEE"))
print(Solution().exist(board=[['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], word="ABCB"))