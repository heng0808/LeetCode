#
# @lc app=leetcode.cn id=541 lang=python3
#
# [541] 反转字符串 II
#

# @lc code=start
class Solution:
    # 双指针o(n/2)
    def reverseStr(self, s: str, k: int) -> str:
        l_index = 0
        r_index = l_index + k - 1
        s_list = list(s)
        while l_index < len(s_list): 
            start = l_index
            remain_l = len(s_list) - l_index
            r_index = l_index + min(remain_l - 1, k - 1)
            while l_index < r_index:
                charactor = s_list[l_index]
                s_list[l_index] = s_list[r_index]
                s_list[r_index] = charactor
                l_index = l_index + 1
                r_index = r_index - 1
            l_index = start + 2 * k
            r_index = l_index + k - 1
        ans = ''
        for charactor in s_list:
            ans = ans + charactor
        return ans
    # 栈遍历 o(n)
    # def reverseStr(self, s: str, k: int) -> str:
    #     _ans = ''
    #     _range = range(0, 2 * k)
    #     while True:
    #         remain_l = len(s) - _range.start
    #         if remain_l < 1:
    #             break
    #         else:
    #             _range = range(_range.start, _range.start + min(remain_l, 2 * k))
    #         stack = []
    #         for index in _range:
    #             if index % (2 * k) < k:
    #                 stack.append(s[index])
    #             else:
    #                 if len(stack) > 0:
    #                     while len(stack) > 0:
    #                         charactor = stack.pop()
    #                         _ans = _ans + charactor
    #                 _ans = _ans + s[index]
    #         while len(stack) > 0:
    #             charactor = stack.pop()
    #             _ans = _ans + charactor
    #         _range = range(_range.start + 2 * k, _range.start + 2 * k + 2 * k)
    #     return _ans
# @lc code=end
print(Solution().reverseStr('abcdefg', 2))