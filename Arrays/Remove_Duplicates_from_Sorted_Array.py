# LeetCode 26 - Remove Duplicates from Sorted Array

# Difficulty: Easy

# Topic: Array, Two Pointers

class Solution:

    def removeDuplicates(self, nums):

        k = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1

        return k

# Time Complexity: O(n)

# Space Complexity: O(1)