class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> [int]:
        # Solution 1
        ans = []
        while len(ans) < num_people:
            ans.append(0)
        
        times = 0
        while candies > 0:
            times = times + 1
            ans[(times - 1) % num_people] = ans[(times - 1) % num_people] + (times if times < candies else candies)
            candies = candies - times
        return ans

print("result = " + str(Solution().distributeCandies(10, 3)))