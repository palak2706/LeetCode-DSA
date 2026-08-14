# LeetCode 136 - Single Number

# Difficulty: Easy

# Topic: Array, Bit Manipulation, XOR

class Solution:

    def singleNumber(self, nums):

        result = 0

        for num in nums:
            result ^= num

        return result

# Time Complexity: O(n)

# Space Complexity: O(1)