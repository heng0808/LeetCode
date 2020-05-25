class Solution:
    def replaceSpace(self, s: str) -> str:
        arr = []
        for character in s:
            if character == ' ':
                arr.append('%20')
            else:
                arr.append(character)
        return ''.join(arr)