# LeetCode 2220 - Minimum Bit Flips to Convert Number

# Difficulty: Easy

# Topic: Bit Manipulation, XOR

class Solution:

    def minBitFlips(self, start, goal):

        x = start ^ goal
        count = 0

        while x:
            count += x & 1
            x >>= 1

        return count

# Time Complexity: O(log n)

# Space Complexity: O(1)