"""
LeetCode Problem: 
1512. Number of Good Pairs

Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.
"""

from typing import List

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hashmap={}
        count=0
        for num in nums:
            if num in hashmap:
                count+=hashmap[num]
                hashmap[num]+=1
            else:
                hashmap[num]=1
        
        return count