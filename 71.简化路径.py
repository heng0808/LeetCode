#
# @lc app=leetcode.cn id=71 lang=python3
#
# [71] 简化路径
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        splits = path.split('/')
        split_paths = []    
        for folder in splits:
            if len(folder) == 0:
                continue
            elif folder == '.':
                continue
            elif folder == '..':
                if len(split_paths) > 0:
                    split_paths.pop()
            else:
                split_paths.append(folder)
        
        path = ''
        for folder in split_paths:
            path = path + '/' + folder
        return path if len(path) > 0 else '/'
        
# @lc code=end
print(Solution().simplifyPath('/home//foo/'))
print(Solution().simplifyPath('/home/'))
print(Solution().simplifyPath('/../'))
print(Solution().simplifyPath('/a/../../b/../c//.//'))
print(Solution().simplifyPath('/a/./b/../../c/'))

