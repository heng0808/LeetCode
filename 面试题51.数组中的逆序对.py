from typing import List
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        count = 0
        def merge(left_vals:[int], right_vals:[int]) -> [int]:
            nonlocal count
            arr = []
            l_i = 0
            r_i = 0
            while l_i < len(left_vals) or r_i < len(right_vals):
                if l_i < len(left_vals) and r_i < len(right_vals):
                    if left_vals[l_i] > right_vals[r_i]:
                        arr.append(left_vals[l_i])
                        count = count + len(right_vals) - r_i
                        l_i = l_i + 1
                    else:
                        arr.append(right_vals[r_i])
                        r_i = r_i + 1
                elif l_i >= len(left_vals):
                    arr.append(right_vals[r_i])
                    r_i = r_i + 1
                elif r_i >= len(right_vals):
                    arr.append(left_vals[l_i])
                    l_i = l_i + 1
            return arr
        def sort(vals:[int]) -> [int]:
            if len(vals) <= 1:
                return vals
            else:
                mid = len(vals) // 2
                left_vals = sort(vals[0:mid])
                right_vals = sort(vals[mid:])
                return merge(left_vals, right_vals)
        nums = sort(nums)
        return count

print(Solution().reversePairs([]))

