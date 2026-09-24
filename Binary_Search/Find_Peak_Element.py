# LeetCode 162 - Find Peak Element

# Difficulty: Medium

# Topic: Binary Search, Arrays

class Solution:
    def findPeakElement(self, nums):
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid

        return left

# Time Complexity: O(log n)
# Space Complexity: O(1)