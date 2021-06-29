#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#
# 1、如果当前位置能到达，那么他能到达的最远位置为i+nums[i]
# 2、如果当前遍历超过最大距离了，那么则代表无法到达 
#
from typing import List
# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        distance = 0
        for i in range(0, len(nums)):
            if i > distance:
                return False
            distance = max(distance, i + nums[i])
        return True
# @lc code=end˜