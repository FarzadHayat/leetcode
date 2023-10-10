# https://leetcode.com/problems/binary-search


# O(n log n) time, O(1) space
# Binary search iterative solution
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            # alternative to avoid integer overflow: l + (r - l) // 2
            mid = (r + l) // 2
            if target < nums[mid]:
                r = mid - 1
            elif target > nums[mid]:
                l = mid + 1
            else:
                return mid
        return -1


# O(n log n) time, O(log n) space
# Binary search recursive solution
class Solution:
    def search(self, nums: list[int], target: int, l=0, r=None) -> int:
        if r is None:
            r = len(nums) - 1
        # alternative to avoid integer overflow: l + (r - l) // 2
        mid = (l + r) // 2
        if l > r:
            return -1
        elif target < nums[mid]:
            return self.search(nums, target, l, mid - 1)
        elif target > nums[mid]:
            return self.search(nums, target, mid + 1, r)
        else:
            return mid


print(Solution().search(nums=[-1, 0, 3, 5, 9, 12], target=9) == 4)
print(Solution().search(nums=[-1, 0, 3, 5, 9, 12], target=2) == -1)
print(Solution().search(nums=[-1, 0, 3, 5, 9], target=9) == 4)
print(Solution().search(nums=[-1, 0, 3, 5, 9], target=3) == 2)
print(Solution().search(nums=[-1, 0, 3, 5, 9], target=-1) == 0)
print(Solution().search(nums=[-1, 0, 3, 5, 9, 12], target=5) == 3)
print(Solution().search(nums=[], target=0) == -1)
print(Solution().search(nums=[0], target=0) == 0)
print(Solution().search(nums=[1, 2, 3], target=1) == 0)
print(Solution().search(nums=[1, 2, 3], target=2) == 1)
print(Solution().search(nums=[1, 2, 3], target=3) == 2)
print(Solution().search(nums=[1, 2, 3], target=4) == -1)
