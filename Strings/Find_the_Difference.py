# LeetCode 389 - Find the Difference

# Difficulty: Easy

# Topic: String, Bit Manipulation

class Solution:

    def findTheDifference(self, s, t):

        result = 0

        for char in s:
            result ^= ord(char)

        for char in t:
            result ^= ord(char)

        return chr(result)

# Time Complexity: O(n)

# Space Complexity: O(1)