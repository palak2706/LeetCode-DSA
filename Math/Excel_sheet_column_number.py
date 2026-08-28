# LeetCode 171 - Excel Sheet Column Number

# Difficulty: Easy
# Topic: Math / String / Base Conversion

class Solution:

    def titleToNumber(self, columnTitle: str) -> int:
        result = 0

        for char in columnTitle:
            result = result * 26 + (ord(char) - ord('A') + 1)

        return result


# Time Complexity: O(n)
# Space Complexity: O(1)