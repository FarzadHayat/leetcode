# O(n) time, O(1) space
# My solution
class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        result = 0
        l, r = 0, n - 1
        maxL, maxR = 0, 0

        while l <= r:
            highest = min(maxL, maxR)
            if maxL <= maxR:
                result += max(highest - height[l], 0)
                maxL = max(maxL, height[l])
                l += 1
            else:
                result += max(highest - height[r], 0)
                maxR = max(maxR, height[r])
                r -= 1
        
        return result

# O(n) time, O(1) space
# NeetCode's solution (slightly easier to read)
class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        result = 0
        l, r = 0, n - 1
        maxL, maxR = height[l], height[r]

        while l < r:
            if maxL < maxR:
                l += 1
                maxL = max(maxL, height[l])
                result += maxL - height[l]
            else:
                r -= 1
                maxR = max(maxR, height[r])
                result += maxR - height[r]
        
        return result

print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1])) # 6
print(Solution().trap([4,2,0,3,2,5])) # 9