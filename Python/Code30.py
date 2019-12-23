class Solution:
    def findSubstring(self, s: str, words: [str]) -> [int]:
        if len(words) == 0:
            return []
        if len(s) < int(len(words) * len(words[0])):
            return []
        wordmap = {}
        wordTotalLength = int(len(words) * len(words[0]))
        wordSingleLength = int(len(words[0]))
        for word in words:
            value = wordmap.get(word, 0)
            wordmap[word] = value + 1
        wordIndexs = []
        for i in range(0, len(s) - wordTotalLength + 1):
            windowmap = {}
            for j in range(i, i + wordTotalLength, wordSingleLength):
                word = s[j:j+wordSingleLength]
                totalCount = wordmap.get(word, False)
                currentCount = windowmap.get(word, 0)
                if totalCount and currentCount < totalCount:
                    windowmap[word] = currentCount + 1
                    if j - i == wordTotalLength - wordSingleLength:
                        wordIndexs.append(i)
                else:
                    break
        return wordIndexs
print(Solution().findSubstring("barfoothefoobarman", ["foo","bar"]))
print(Solution().findSubstring("wordgoodgoodgoodbestword", ["word","good","best","word"]))
print(Solution().findSubstring("wordgoodgoodgoodbestword", ["word","good","best","good"]))