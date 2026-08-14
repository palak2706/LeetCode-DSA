# LeetCode 1356 - Sort Integers by The Number of 1 Bits

# Difficulty: Easy

# Topic: Array, Sorting, Bit Manipulation

class Solution:

    def sortByBits(self, arr):

        arr.sort(key=lambda x: (bin(x).count('1'), x))

        return arr

# Time Complexity: O(n log n)

# Space Complexity: O(n)