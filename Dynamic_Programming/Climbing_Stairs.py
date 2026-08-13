# LeetCode 70 - Climbing Stairs

# Difficulty: Easy

# Topic: Dynamic Programming, Math

class Solution:

    def climbStairs(self, n):

        if n <= 2:
            return n

        a, b = 1, 2

        for i in range(3, n + 1):
            a, b = b, a + b

        return b

# Time Complexity: O(n)

# Space Complexity: O(1)