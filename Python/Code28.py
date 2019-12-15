class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        dict = {}
        for i, j in zip(range(0, len(haystack)), range(len(needle) - 1, len(haystack))):
            if haystack[i] == needle[0] and haystack[j] == needle[j-i]:
                dict.update({str(i): haystack[i:j+1]})
        index = None
        for (k, v) in dict.items():
            if v == needle:
                if index is None or int(k) < index:
                    index = int(k)
        return -1 if index is None else index
print(Solution().strStr("123", ""))