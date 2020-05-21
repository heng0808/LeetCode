#
# @lc app=leetcode.cn id=443 lang=python3
#
# [443] 压缩字符串
#
from typing import List
# @lc code=start
class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 1
        count = 0
        compare_char = None
        for j in range(0, len(chars)):
            character = chars[j]
            if compare_char == None:
                compare_char = character
                i = 0
                count = 1
            else:
                if character == compare_char:
                    count = count + 1
                else:
                    if count > 1:
                        while count > 0:
                            i = i + 1
                            num = count
                            while num // 10 > 0:
                                num = num // 10
                            chars[i] = num
                    compare_char = character
                    i = i + 1
                    count = 1
                    single = True
                    chars[i] = character
        if compare_char == None:
            return 0
        else:
            return i + 1
# @lc code=end
print(Solution().compress(["a","a","a","a","a","a","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","c","c","c","c","c","c","c","c","c","c","c","c","c","c"]))

