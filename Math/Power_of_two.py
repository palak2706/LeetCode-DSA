# LeetCode 231 - Power of Two
# Difficulty: Easy
# Topic: Math / Number Theory

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False

        while n % 2 == 0:
            n = n // 2

        return n == 1


# Time Complexity: O(log n)
# Space Complexity: O(1)