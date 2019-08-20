class Solution:
    def romanToInt(self, s: str) -> int:
        map = {
            "M": 1000,
            "CM": 900,
            "D": 500,
            "CD": 400,
            "C": 100,
            "XC": 90,
            "L": 50,
            "XL": 40,
            "X": 10,
            "IX": 9,
            "V": 5,
            "IV": 4,
            "I": 1
        }
        sum = 0

        while len(s) > 0:
            for roman, num in map.items():
                if s.startswith(roman):
                    sum = sum + num
                    s = s.replace(roman, "", 1)
                    break
        return sum

Solution().romanToInt('III')