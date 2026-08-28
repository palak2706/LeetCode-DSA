# LeetCode 191 - Number of 1 Bits

# Difficulty: Easy
# Topic: Bit Manipulation / Binary

class Solution:

    def hammingWeight(self, n: int) -> int:
        count = 0

        while n > 0:
            count += n & 1
            n = n >> 1

        return count


# Time Complexity: O(log n)
# Space Complexity: O(1)