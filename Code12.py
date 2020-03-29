class Solution:
    def intToRoman(self, num: int) -> str:
        remainder = num
        roman = ""
        if int(num / 1000) > 0:
            roman = roman + "M" * int(num / 1000)
            remainder = num % 1000
        if remainder >= 900:
            roman = roman + "CM"
            remainder = remainder - 900

        if int(remainder / 500) > 0:
            roman = roman + "D" * int(remainder / 500)
            remainder = remainder % 500
        if remainder >= 400:
            roman = roman + "CD"
            remainder = remainder - 400

        if int(remainder / 100) > 0:
            roman = roman + "C" * int(remainder / 100)
            remainder = remainder % 100
        if remainder >= 90:
            roman = roman + "XC"
            remainder = remainder - 90

        if int(remainder / 50) > 0:
            roman = roman + "L" * int(remainder / 50)
            remainder = remainder % 50
        if remainder >= 40:
            roman = roman + "XL"
            remainder = remainder - 40

        if int(remainder / 10) > 0:
            roman = roman + "X" * int(remainder / 10)
            remainder = remainder % 10
        if remainder >= 9:
            roman = roman + "IX"
            remainder = remainder - 9

        if int(remainder / 5) > 0:
            roman = roman + "V" * int(remainder / 5)
            remainder = remainder % 5
        if remainder >= 4:
            roman = roman + "IV"
            remainder = remainder - 4

        roman = roman + "I" * int(remainder)

        return roman

Solution().intToRoman(444)