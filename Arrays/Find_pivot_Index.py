# LeetCode 724 - Find Pivot Index

# Difficulty: Easy

# Topic: Array, Prefix Sum

class Solution:

    def pivotIndex(self, nums):

        total = sum(nums)
        left_sum = 0

        for i in range(len(nums)):
            right_sum = total - left_sum - nums[i]

            if left_sum == right_sum:
                return i

            left_sum += nums[i]

        return -1

# Time Complexity: O(n)

# Space Complexity: O(1)