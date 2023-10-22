from typing import List


# O(n^3) time, O(1) space
class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        res = -1
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] < nums[j] and nums[j] > nums[k]:
                        if res == -1:
                            res = nums[i] + nums[j] + nums[k]
                        else:
                            res = min(res, nums[i] + nums[j] + nums[k])
        return res


print(Solution().minimumSum([8, 6, 1, 5, 3]) == 9)
print(Solution().minimumSum([5, 4, 8, 7, 10, 2]) == 13)
print(Solution().minimumSum([6, 5, 4, 3, 4, 5]) == -1)
