# LeetCode 283 - Move Zeroes
# Difficulty: Easy
# Topic: Array, Two Pointers

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1


# Time Complexity: O(n)
# Space Complexity: O(1)