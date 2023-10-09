# https://leetcode.com/problems/largest-rectangle-in-histogram


# O(n^2) time, O(1) space
# Brute force solution
class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        best = 0
        for i in range(len(heights)):
            min_height = float("inf")
            for j in range(i, len(heights)):
                min_height = min(min_height, heights[j])
                area = (j - i + 1) * min_height
                best = max(best, area)
        return int(best)


# O(n) time, O(n) space
# Stack solution
class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        best = 0
        # monotically non-decreasing stack
        stack = []  # (idx, height) pair
        for i in range(len(heights)):
            start = i
            # loop while stack not empty and current height is less than height at top of stack
            while stack and heights[i] < stack[-1][1]:
                # pop element at top of stack and calculate its max area
                idx, height = stack.pop()
                area = (i - idx) * height
                best = max(best, area)
                start = idx
            # push new element to stack using maximum width possible
            stack.append((start, heights[i]))
        # calculate max area of remaining elements in stack
        for idx, height in stack:
            area = (len(heights) - idx) * height
            best = max(best, area)
        return best


print(Solution().largestRectangleArea([2, 1, 5, 6, 2, 3]) == 10)
print(Solution().largestRectangleArea([2, 4]) == 4)
print(Solution().largestRectangleArea([1]) == 1)
print(Solution().largestRectangleArea([1, 2]) == 2)
print(Solution().largestRectangleArea([1, 2, 3]) == 4)
print(Solution().largestRectangleArea([1, 2, 3, 4]) == 6)
print(Solution().largestRectangleArea([1, 2, 3, 4, 5]) == 9)
print(Solution().largestRectangleArea([1, 2, 3, 2, 1]) == 6)
print(Solution().largestRectangleArea([3, 2, 1, 2, 3]) == 5)
print(Solution().largestRectangleArea([3, 2, 0, 2, 3]) == 4)
print(Solution().largestRectangleArea([3, 2, 0, 5]) == 5)
print(Solution().largestRectangleArea([5, 6, 7]) == 15)
print(Solution().largestRectangleArea([3, 2, 5, 6]) == 10)
print(Solution().largestRectangleArea([2, 3, 5, 6, 2, 3]) == 12)
print(Solution().largestRectangleArea([3, 2, 5, 6, 3, 2]) == 12)
