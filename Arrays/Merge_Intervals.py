# LeetCode 56 - Merge Intervals
# Difficulty: Medium
# Topics: Array, Sorting, Greedy


from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort intervals by starting time
        intervals.sort(key=lambda x: x[0])

        merged = []

        for interval in intervals:
            # If no overlap, add the interval
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # Merge overlapping intervals
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged


# Time Complexity: O(n log n)
# Space Complexity: O(n)    