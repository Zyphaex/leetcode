"""
LeetCode Problem: 
0053. Maximum Subarray

Given an integer array nums, find the subarray with the largest sum, and return its sum.
"""

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currentSum = nums[0]

        for num in nums[1:]:
            currentSum = max(num, currentSum + num)
            maxSum = max(maxSum, currentSum)

        return maxSum