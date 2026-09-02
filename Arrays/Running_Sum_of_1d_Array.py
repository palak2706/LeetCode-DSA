# LeetCode 1480 - Running Sum of 1d Array

# Difficulty: Easy

# Topic: Array, Prefix Sum

class Solution:

    def runningSum(self, nums):

        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i - 1]

        return nums

# Time Complexity: O(n)

# Space Complexity: O(1)