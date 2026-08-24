# LeetCode 1046 - Last Stone Weight

# Difficulty: Easy

# Topic: Heap, Priority Queue

class Solution:
    def lastStoneWeight(self, stones):
        import heapq

        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            first = -heapq.heappop(heap)
            second = -heapq.heappop(heap)

            if first != second:
                heapq.heappush(heap, -(first - second))

        return -heap[0] if heap else 0

# Time Complexity: O(n log n)

# Space Complexity: O(n)