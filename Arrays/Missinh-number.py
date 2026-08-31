# LeetCode 268 - Missing Number

# Difficulty: Easy

# Topic: Array, Math, Bit Manipulation

class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        
        return expected_sum - actual_sum

# Time Complexity: O(n)
# Space Complexity: O(1)