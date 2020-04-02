#
# @lc app=leetcode.cn id=68 lang=python3
#
# [68] 文本左右对齐
#
from typing import List
# @lc code=start
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        rowWords = []
        rowWordLengths = []
        rowWord = []
        rowWordLength = 0
        remaindWordLength = maxWidth
        for index in range(0, len(words)):
            word = words[index]
            if len(word) > remaindWordLength:
                # 不可以插入当前行
                rowWords.append(rowWord)
                rowWordLengths.append(rowWordLength)
                rowWord = []
                rowWordLength = 0
                remaindWordLength = maxWidth
            rowWord.append(word)
            remaindWordLength = remaindWordLength - 1 - len(word)
            rowWordLength = rowWordLength + len(word)
        if len(rowWord) != 0:
            rowWords.append(rowWord)
            rowWordLengths.append(rowWordLength)
        sentences = []   
        for index in range(0, len(rowWords)):
            rowWordLength = rowWordLengths[index]
            rowWord = rowWords[index]
            spaceLength = maxWidth - rowWordLength
            if index == len(rowWords) - 1:
                sentence = ''
                for index in range(0, len(rowWord)):
                    word = rowWord[index]
                    if index != 0:
                        sentence = sentence + ' ' + word
                        spaceLength = spaceLength - 1
                    else:
                        sentence = word
                sentence = sentence + ' ' * spaceLength
                sentences.append(sentence)
            else:
                if len(rowWord) == 1:
                    sentences.append(rowWord[0] + ' ' * spaceLength)
                else:
                    if len(rowWord) <= 2:
                        separateSpaceLength = spaceLength
                        remaindSpaceLength = 0
                    else:
                        separateSpaceLength = spaceLength // (len(rowWord) - 1)
                        remaindSpaceLength = spaceLength % (len(rowWord) - 1)
                    sentence = ''
                    for index in range(0, len(rowWord)):
                        word = rowWord[index]
                        if index != 0:
                            sentence = sentence + ' ' * separateSpaceLength + (' ' if remaindSpaceLength > 0 else '') + word
                            remaindSpaceLength = remaindSpaceLength - 1
                        else:
                            sentence = word
                        if index == len(rowWord) - 1:
                            # 最后一个
                            sentences.append(sentence)
        return sentences
# @lc code=end
print(Solution().fullJustify(["What","must","be","acknowledgment","shall","be"], 16))
# print(Solution().fullJustify(["Science","is","what","we","understand","well","enough","to","explain", "to","a","computer.","Art","is","everything","else","we","do"], 20))
