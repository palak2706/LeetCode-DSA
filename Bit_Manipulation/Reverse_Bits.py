# LeetCode 190 - Reverse Bits

# Difficulty: Easy

# Topic: Bit Manipulation

class Solution:

    def reverseBits(self, n):

        result = 0

        for i in range(32):
            result = (result << 1) | (n & 1)
            n >>= 1

        return result

# Time Complexity: O(1)

# Space Complexity: O(1)