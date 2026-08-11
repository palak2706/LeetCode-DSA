# LeetCode 1342 - Number of Steps to Reduce a Number to Zero

# Difficulty: Easy

# Topic: Math, Bit Manipulation

class Solution:

    def numberOfSteps(self, num):

        steps = 0

        while num > 0:
            if num % 2 == 0:
                num //= 2
            else:
                num -= 1

            steps += 1

        return steps

# Time Complexity: O(log n)

# Space Complexity: O(1)