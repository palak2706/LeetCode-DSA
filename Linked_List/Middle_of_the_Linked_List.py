# LeetCode 876 - Middle of the Linked List

# Difficulty: Easy

# Topic: Linked List, Two Pointers

class Solution:

    def middleNode(self, head):

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

# Time Complexity: O(n)

# Space Complexity: O(1)