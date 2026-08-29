# LeetCode 258 - Add Digits

# Difficulty: Easy
# Topic: Math / Digit Manipulation

class Solution:

    def addDigits(self, num: int) -> int:
        while num >= 10:
            total = 0

            while num > 0:
                digit = num % 10
                total += digit
                num = num // 10

            num = total

        return num


# Time Complexity: O(log n)
# Space Complexity: O(1)