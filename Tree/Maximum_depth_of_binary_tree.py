# LeetCode 104 - Maximum Depth of Binary Tree

# Difficulty: Easy

# Topic: Tree, DFS, Recursion

class Solution:
    def maxDepth(self, root):
        if not root:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return 1 + max(left, right)

# Time Complexity: O(n)

# Space Complexity: O(h)