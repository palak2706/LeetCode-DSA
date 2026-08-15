# LeetCode 137 - Single Number II

# Difficulty: Medium

# Topic: Bit Manipulation, Bitwise Operations

class Solution:

    def singleNumber(self, nums):

        ones = 0
        twos = 0

        for num in nums:
            ones = (ones ^ num) & ~twos
            twos = (twos ^ num) & ~ones

        return ones

# Time Complexity: O(n)

# Space Complexity: O(1)