# LeetCode 169 - Majority Element

# Difficulty: Easy

# Topic: Arrays, Hash Table, Boyer-Moore Voting Algorithm

class Solution:
    def majorityElement(self, nums):
        count = 0
        candidate = 0

        for num in nums:
            if count == 0:
                candidate = num

            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate

# Time Complexity: O(n)
# Space Complexity: O(1)