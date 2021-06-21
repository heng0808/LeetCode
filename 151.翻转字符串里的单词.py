#
# @lc app=leetcode.cn id=151 lang=python3
#
# [151] 翻转字符串里的单词
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        result = ""
        s_stack = [] # 句子栈
        w_queue = [] # 单词队列
        for letter in s:
            if letter == ' ':
                if len(w_queue) > 0:
                    s_stack.append(w_queue)
                w_queue = []
            else:
                w_queue.append(letter)
        
        if len(w_queue) > 0:
            s_stack.append(w_queue)

        while len(s_stack) > 0:
            w_queue = s_stack.pop()
            while len(w_queue) > 0:
                result += w_queue.pop(0)
            if len(s_stack) > 0:
                result += ' '

        return result
# @lc code=end

print(Solution().reverseWords("the sky is blue"))
print(Solution().reverseWords("  hello world  "))
print(Solution().reverseWords("a good   example"))
print(Solution().reverseWords("  Bob    Loves  Alice   "))
