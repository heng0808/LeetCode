class Solution:
    def longestCommonPrefix(self, strs: [str]) -> str:
        max_str = ""
        index = 0
        run = True
        while run:
            try:
                char = strs[0][index]
            except:
                run = False
            else:
                if len(strs) > 1:
                    for str in strs[1:]:
                        try:
                            char_other = str[index]
                            if char != char_other:
                                run = False
                                break
                        except:
                            run = False
                            break
                if run:
                    max_str = max_str + char
                    index = index + 1
        return max_str

Solution().longestCommonPrefix(["abc", "abcd", "abcde"])