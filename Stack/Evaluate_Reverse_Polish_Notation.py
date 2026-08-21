# LeetCode 150 - Evaluate Reverse Polish Notation
# Difficulty: Medium
# Topic: Stack

class Solution:
    def evalRPN(self, tokens):
        stack = []

        for token in tokens:
            if token not in "+-*/":
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()

                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                else:
                    stack.append(int(a / b))

        return stack[-1]

    # Time Complexity: O(n)
# Space Complexity: O(n)