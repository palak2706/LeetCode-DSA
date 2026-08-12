# LeetCode 1295 - Find Numbers with Even Number of Digits

# Difficulty: Easy

# Topic: Array, Math

class Solution:

    def findNumbers(self, nums):

        count = 0

        for num in nums:
            if len(str(num)) % 2 == 0:
                count += 1

        return count

# Time Complexity: O(n)

# Space Complexity: O(1)