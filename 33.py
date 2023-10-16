# https://leetcode.com/problems/search-in-rotated-sorted-array


# O(log n) time, O(1) space
# Binary search solution
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if target == nums[m]:
                return m
            # m is in the left sorted portion
            if nums[l] <= nums[m]:
                # target is within the left sorted portion, so search left
                if nums[l] <= target < nums[m]:
                    r = m - 1
                # target is not in the left sorted portion, so search right
                else:
                    l = m + 1
            # m is in the right sorted portion
            else:
                # target is within the right sorted portion, so search right
                if nums[m] < target <= nums[r]:
                    l = m + 1
                # target is not in the right sorted portion, so search left
                else:
                    r = m - 1
        return -1


print(Solution().search(nums=[4, 5, 6, 7, 0, 1, 2], target=0) == 4)
print(Solution().search(nums=[4, 5, 6, 7, 0, 1, 2], target=7) == 3)
print(Solution().search(nums=[4, 5, 6, 7, 0, 1, 2], target=4) == 0)
print(Solution().search(nums=[4, 5, 6, 7, 0, 1, 2], target=3) == -1)

print(Solution().search(nums=[6, 7, 0, 1, 2, 3, 4], target=7) == 1)
print(Solution().search(nums=[6, 7, 0, 1, 2, 3, 4], target=1) == 3)
print(Solution().search(nums=[6, 7, 0, 1, 2, 3, 4], target=3) == 5)
print(Solution().search(nums=[6, 7, 0, 1, 2, 3, 4], target=5) == -1)

print(Solution().search(nums=[1], target=0) == -1)
print(Solution().search(nums=[1], target=1) == 0)

print(Solution().search(nums=[1, 2, 3, 4, 5], target=1) == 0)
print(Solution().search(nums=[1, 2, 3, 4, 5], target=3) == 2)
print(Solution().search(nums=[1, 2, 3, 4, 5], target=5) == 4)
