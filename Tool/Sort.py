import random

class Sort:
    @staticmethod
    def quick(nums:[int]):
        stack = [(0, len(nums) - 1)] if len(nums) > 0 else []
        while len(stack) > 0:
            (start, end) = stack.pop()
            if end <= start:
                continue
            temp, low, high = nums[start], start, end
            while low < high:
                while low < high and nums[low] < temp:
                    low = low + 1
                while high > low and nums[high] >= temp:
                    high = high - 1
                num = nums[high]
                nums[high] = nums[low]
                nums[low] = num
            if start < low and high < end:
                stack.append((start, low - 1))
                stack.append((high, end))                
                
    @staticmethod
    def merge(nums:[int]):
        pass

nums = []
while len(nums) < 2:
    nums.append(random.randint(0, 100))
print("before sort: " + str(nums))
Sort.quick(nums)
print("after sort: " + str(nums))