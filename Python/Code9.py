class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        front_half = ''
        behind_half = ''
        if len(x_str) % 2 == 0:
            front_half = x_str[0:round(len(x_str) / 2)]
            behind_half = x_str[:-round(len(x_str) / 2) - 1:-1]
        else:
            front_half = x_str[0:round(len(x_str) / 2)]
            behind_half = x_str[:-round(len(x_str) / 2) - 1:-1]
        return front_half == behind_half

print(Solution().isPalindrome(5131221315))
