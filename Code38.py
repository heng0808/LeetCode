from typing import List

class Solution:
    def countAndSay(self, n: int) -> str:
        i = 1
        current_str = '1'
        while i < n:
            i = i + 1
            map_arr = []
            for character in current_str:
                if len(map_arr) == 0:
                    map_arr.append({
                        "character": character,
                        "count": 1
                    })
                else:
                    last_character = map_arr[-1]["character"]
                    last_character_count = count = map_arr[-1]["count"]
                    if last_character == character:
                        map_arr[-1] = {
                            "character": character,
                            "count": last_character_count + 1
                        }
                    else:
                        map_arr.append({
                            "character": character,
                            "count": 1
                        })
            next_str = ''
            for map in map_arr:
                next_str = next_str + str(map["count"]) + map["character"]
            current_str = next_str
        return current_str

print(Solution().countAndSay(7))