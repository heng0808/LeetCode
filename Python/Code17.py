class Solution:
    def letterCombinations(self, digits: str) -> [str]:
        map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        letters = []
        def nextNumber(letter:str, next:str):
            if next == None or len(next) == 0:
                if len(letter) > 0:
                    letters.append(letter)
            else:
                for char in map[next[0]]:
                    combine = letter + char
                    nextNumber(combine, next[1:])

        nextNumber("", next=digits)
        return letters

print(Solution().letterCombinations(""))