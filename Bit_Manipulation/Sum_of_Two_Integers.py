# LeetCode 371 - Sum of Two Integers

# Difficulty: Medium

# Topic: Bit Manipulation, Bitwise Operators

class Solution:

    def getSum(self, a, b):

        mask = 0xFFFFFFFF

        while b:
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask

        if a > 0x7FFFFFFF:
            a = ~(a ^ mask)

        return a

# Time Complexity: O(1)

# Space Complexity: O(1)