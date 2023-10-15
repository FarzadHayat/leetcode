# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array


# O(log n) time, O(1) space
# Binary search to find point of inflection
class Solution:
    def findMin(self, nums: list[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            if nums[l] < nums[r]:
                return nums[l]
            m = l + (r - l) // 2
            if nums[l] <= nums[m]:
                l = m + 1
            else:
                r = m
        return nums[l]


print(Solution().findMin([1, 2, 3, 4, 5]) == 1)
print(Solution().findMin([2, 3, 4, 5, 1]) == 1)
print(Solution().findMin([3, 4, 5, 1, 2]) == 1)
print(Solution().findMin([4, 5, 1, 2, 3]) == 1)
print(Solution().findMin([5, 1, 2, 3, 4]) == 1)
print(Solution().findMin([4, 5, 1, 2, 3, 4]) == 1)
print(Solution().findMin([5]) == 5)
print(Solution().findMin([1, 10]) == 1)
print(Solution().findMin([10, 1]) == 1)
print(Solution().findMin([4, 5, 6, 7, 0, 1, 2]) == 0)
print(Solution().findMin([11, 13, 15, 17]) == 11)
