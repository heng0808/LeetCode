from typing import List
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        if len(s) <= 2:
            return len(s)
        left = 0
        right = 1
        count_map = {s[left]: 1}
        character_set = {s[left]}
        max_len = 0
        while True:
            character = s[right]
            if character in character_set:
                count_map[character] = count_map[character] + 1 if character in count_map else 1
            else:
                if len(character_set) == 2:
                    max_len = max(max_len, right - left)
                    while True:
                        remove_character = s[left]
                        count_map[remove_character] = count_map[remove_character] - 1
                        left = left + 1
                        if count_map[remove_character] == 0:
                            character_set.remove(remove_character)
                            break
                character_set.add(character)
                count_map[character] = 1
            right += 1
            if right == len(s):
                break
        return max(max_len, right - left)

# print(Solution().lengthOfLongestSubstringTwoDistinct("eceba"))
# print(Solution().lengthOfLongestSubstringTwoDistinct("ccaabbb"))
# print(Solution().lengthOfLongestSubstringTwoDistinct("ccb"))
print(Solution().lengthOfLongestSubstringTwoDistinct("cc"))
# print(Solution().lengthOfLongestSubstringTwoDistinct("c"))