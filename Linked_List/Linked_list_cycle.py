# LeetCode 141 - Linked List Cycle

# Difficulty: Easy

# Topic: Linked List, Two Pointers

class Solution:
    def hasCycle(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False

# Time Complexity: O(n)

# Space Complexity: O(1)