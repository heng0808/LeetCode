#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] 乘积最大子数组
#
from typing import List
# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = nums[0]
        product = nums[0]
        left = 0 # 左边坐标
        right = 0 # 右边坐标
        for index in range(1, len(nums)):
            num = nums[index]
            if num > max_product:
                max_product = num
            if num == 0:
                # 当前为0的时候，找出左侧range最大的
                l_max_product = self.searchMaxProduct(nums, left, right, product)
                if l_max_product > max_product:
                    max_product = l_max_product
                right = index
                left = index
                product = nums[index]
            else:
                if product == 0:
                    right = index
                    left = index
                    product = nums[index]
                else:
                    right = index
                    product = product * num

        # 找出最后的range的最大的
        t_max_product = self.searchMaxProduct(nums, left, right, product)
        if t_max_product > max_product:
            max_product = t_max_product
        return max_product

    def searchMaxProduct(self, nums: List[int], left: int, right: int, product: int) -> int:
        if right > left:
            left_product = self.searchMaxProduct(nums, left+1, right, product // nums[left])
            right_product = self.searchMaxProduct(nums, left, right-1, product // nums[right])
            sub_maxProduct = left_product if left_product > right_product else right_product
            if sub_maxProduct > product:
                return sub_maxProduct
            else:
                return product
        else:
            return product
        
# @lc code=end
print(Solution().maxProduct([0]))
print(Solution().maxProduct([2,3,-2,4]))
print(Solution().maxProduct([-2,0,-1]))
print(Solution().maxProduct([1,2,3,4]))
print(Solution().maxProduct([2,0,3]))
print(Solution().maxProduct([3,-1,4]))
print(Solution().maxProduct([2,-5,-2,-4,3]))
