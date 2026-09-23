# LeetCode 78 - Subsets

# Difficulty: Medium

# Topic: Arrays, Backtracking, Bit Manipulation

class Solution:
    def subsets(self, nums):
        result = []

        def backtrack(start, current):
            result.append(current[:])

            for i in range(start, len(nums)):
                current.append(nums[i])
                backtrack(i + 1, current)
                current.pop()

        backtrack(0, [])

        return result

# Time Complexity: O(n * 2^n)
# Space Complexity: O(n) excluding the output