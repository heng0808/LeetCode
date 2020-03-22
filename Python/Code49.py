from typing import List, collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = dict()
        for s in strs:
            key = tuple(sorted(s))
            if key in ans.keys():
                ans[key].append(s)
            else:
                ans[key] = [s]
        return list(ans.values())

print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))