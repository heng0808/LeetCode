class Solution:
    def checkRecord(self, s: str) -> bool:
        a_count = 0
        l_last_count = 0
        for char in s:
            if char == 'A':
                a_count = a_count + 1
                l_last_count = 0
            elif char == 'L':
                l_last_count = l_last_count + 1
            else:
                l_last_count = 0
            if a_count > 1 or l_last_count > 2:
                return False
        return True
Solution().checkRecord("LALL")