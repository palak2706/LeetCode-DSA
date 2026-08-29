# LeetCode 202 - Happy Number

# Difficulty: Easy
# Topic: Math / Hash Set / Cycle Detection

class Solution:

    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:
            if n in seen:
                return False

            seen.add(n)

            total = 0
            while n > 0:
                digit = n % 10
                total += digit * digit
                n = n // 10

            n = total

        return True


# Time Complexity: O(log n)
# Space Complexity: O(log n)