# LeetCode 338 - Counting Bits

# Difficulty: Easy

# Topic: Dynamic Programming, Bit Manipulation

class Solution:

    def countBits(self, n):

        ans = [0] * (n + 1)

        for i in range(1, n + 1):
            ans[i] = ans[i >> 1] + (i & 1)

        return ans

# Time Complexity: O(n)

# Space Complexity: O(n)