# LeetCode 693 - Binary Number with Alternating Bits

# Difficulty: Easy

# Topic: Bit Manipulation

class Solution:

    def hasAlternatingBits(self, n):

        prev = n & 1
        n >>= 1

        while n:
            curr = n & 1

            if curr == prev:
                return False

            prev = curr
            n >>= 1

        return True

# Time Complexity: O(log n)

# Space Complexity: O(1)