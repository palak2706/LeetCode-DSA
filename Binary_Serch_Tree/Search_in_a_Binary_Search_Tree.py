# LeetCode 700 - Search in a Binary Search Tree

# Difficulty: Easy

# Topic: Binary Search Tree, Binary Tree

class Solution:
    def searchBST(self, root, val):
        if root is None:
            return None

        if root.val == val:
            return root

        if val < root.val:
            return self.searchBST(root.left, val)

        return self.searchBST(root.right, val)

# Time Complexity: O(h)
# Space Complexity: O(h)