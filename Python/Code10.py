# '.' 匹配任意单个字符
# '*' 匹配零个或多个前面的那一个元素
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if len(s) == 0:
            if len(p) > 0:
                return len(p) > 2 and p.startswith('.*')
            else:
                return True
        else:
            if len(p) == 0:
                return False
            else:
                for char_index in range(0, len(s)):
                    if char_index >= len(p):
                        return False
                    s_char = s[char_index]
                    p_char = p[char_index]
                    if p_char == s_char or p_char == '.':
                        continue
                    elif p_char == '*':
                        try:
                            p_char_pre = p[char_index - 1]
                        except:
                            return False
                        else:
                            if p_char_pre == s_char or p_char_pre == '.':
                                # * 前面添加
                                pre = p[:char_index - 1]
                                next = p[char_index - 1:]
                                p = pre + p_char_pre + next
                                print()
                            else:
                                try:
                                    p_char_next = p[char_index + 1]
                                except:
                                    return False
                                else:
                                    if p_char_next == s_char or p_char_next == '.':
                                        pre = p[:char_index]
                                        next = p[char_index + 1:]
                                        p = pre + next
                                        print()
                                    else:
                                        return False
                    else:
                        try:
                            p_char_next = p[char_index + 1]
                        except:
                            return False
                        else:
                            if p_char_next == '*':
                                try:
                                    pre = p[:char_index]
                                    next = p[char_index + 1 + 1:]
                                    p = pre + next
                                    print()
                                except:
                                    return False
                            else:
                                return False
                p_reduce = p[len(s):]
                for p_reduce_char_index in range(0, len(p_reduce)):
                    p_reduce_char = p_reduce[p_reduce_char_index]
                    if p_reduce_char != "*":
                        try:
                            p_reduce_char_pre = p_reduce[p_reduce_char_index - 1]
                        except:
                            pass
                        try:
                            p_reduce_char_next = p_reduce[p_reduce_char_index + 1]
                        except:
                            return False
                return True

def match(s:str, p:str, index:int):
    try:
        s_char = s[index]
        p_char = p[index]
        if s_char == p_char or p_char == '.':
            return match(s, p, index+1)
        elif p_char == '*':
            pass
        else:
            pass
    except:
        return False