# LeetCode 215 - Kth Largest Element in an Array

# Difficulty: Medium

# Topic: Heap, Priority Queue

class Solution:
    def findKthLargest(self, nums, k):
        import heapq

        heap = []

        for num in nums:
            heapq.heappush(heap, num)

            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]

# Time Complexity: O(n log k)

# Space Complexity: O(k)