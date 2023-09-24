# O(n^2) time, O(1) space
# Brute force option (time limit exceeded on LeetCode)
class Solution:
    def maxArea(self, height: list[int]) -> int:
        n = len(height)
        best = 0
        for l in range(n):
            if (n - 1 - l) * height[l] <= best:
                continue
            for r in range(n - 1, l, -1):
                area = (r - l) * min(height[l], height[r])
                best = max(best, area)
        return best

# O(n) time, O(1) space
# Two pointers solution
class Solution:
    def maxArea(self, height: list[int]) -> int:
        best = 0
        l, r = 0, len(height) - 1
        while l < r:
            area = (r - l) * min(height[l], height[r])
            best = max(best, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return best

print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))
print(Solution().maxArea([1,1]))