# LeetCode 189 - Rotate Array

# Difficulty: Medium

# Topic: Array, Two Pointers

class Solution:
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n

        nums.reverse()

        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])

# Time Complexity: O(n)
# Space Complexity: O(1)