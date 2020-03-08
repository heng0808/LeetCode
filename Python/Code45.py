class Solution:
    def jump(self, nums: [int]) -> int:
        # Solution 1
        # minStepCount = -1

        # def jumpNext(index: int, step: int, stepCount: int): 
        #     if index + step == len(nums) - 1:
        #         # 到最后一个了
        #         nonlocal minStepCount
        #         minStepCount = stepCount + 1 if minStepCount == -1 or minStepCount > stepCount + 1 else minStepCount
        #     elif index + step < len(nums) - 1:
        #         # 没到最后一个了
        #         if stepCount + 1 < minStepCount or minStepCount == -1:
        #             for nextStep in range(1, nums[index + step] + 1):
        #                 jumpNext(index + step, nextStep, stepCount + 1)
                    

        # for step in range(1, nums[0] + 1):
        #     jumpNext(0, step, 0)

        # return minStepCount if minStepCount != -1 else 0

        # Solution 2
        ans = 0
        left = 0
        while left < len(nums) - 1:
            if left + nums[left] >= len(nums) - 1:
                ans = ans + 1
                break
            right = left
            for step in range(1, nums[left] + 1):
                # 下一次最远
                right = left + step if (left + step + nums[left + step]) > (right + nums[right]) else right
            if right == left:
                # 没有能跳过去的
                ans = 0
                break
            else:
                left = right
                ans = ans + 1
        return ans

        # # Solution 3
        # ans = 0
        # right = len(nums) - 1
        # while right > 0:
        #     left = right
        #     for index in range(right, -1, -1):
        #         # 能跳到这里
        #         if right - index <= nums[index]:
        #             left = index if index < left else left
        #     if left == right:
        #         # 没有能调到这里的
        #         ans = 0
        #         break
        #     else:
        #         right = left
        #         ans = ans + 1
        # return ans

# print(Solution().jump([1,2]))
# print(Solution().jump([2,3,1,1,4]))
# print(Solution().jump([0]))
print(Solution().jump([8,2,4,4,4,9,5,2,5,8,8,0,8,6,9,1,1,6,3,5,1,2,6,6,0,4,8,6,0,3,2,8,7,6,5,1,7,0,3,4,8,3,5,9,0,4,0,1,0,5,9,2,0,7,0,2,1,0,8,2,5,1,2,3,9,7,4,7,0,0,1,8,5,6,7,5,1,9,9,3,5,0,7,5]))
