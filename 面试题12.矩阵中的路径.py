from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def findWord(i, j, word_i) -> bool:
            if board[i][j] == word[word_i]:
                character = board[i][j]
                board[i][j] = ''
                if word_i == len(word) - 1:
                    return True
                if i != 0 and findWord(i - 1, j, word_i + 1):
                    return True
                if i < len(board) - 1 and findWord(i + 1, j, word_i + 1):
                    return True
                if j != 0 and findWord(i, j - 1, word_i + 1):
                    return True
                if j < len(board[i]) - 1 and findWord(i, j + 1, word_i + 1):
                    return True
                board[i][j] = character
            return False
        for i in range(0, len(board)):
            for j in range(0, len(board[i])):
                if findWord(i, j, 0):
                    return True
        return False

print(Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], 'ABCCED'))
print(Solution().exist([["a","b"],["c","d"]], 'abcd'))
print(Solution().exist([["a","a"]], 'aaa'))