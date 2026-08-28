# LeetCode 69 - Sqrt(x)

# Difficulty: Easy
# Topic: Binary Search / Math

class Solution:

    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        left = 1
        right = x // 2

        while left <= right:
            mid = (left + right) // 2

            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1

        return right


# Time Complexity: O(log x)
# Space Complexity: O(1)