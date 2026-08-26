# LeetCode 933 - Number of Recent Calls

# Difficulty: Easy

# Topic: Queue, Sliding Window

class RecentCounter:

    def __init__(self):
        from collections import deque
        self.queue = deque()

    def ping(self, t):
        self.queue.append(t)

        while self.queue[0] < t - 3000:
            self.queue.popleft()

        return len(self.queue)

# Time Complexity: O(n) overall
# Space Complexity: O(n)