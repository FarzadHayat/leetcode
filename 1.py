# O(n) time, O(n) space
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        lst = set()
        for i in range(n):
            curr = nums[i]
            if (target - curr) in lst:
                return [i, nums.index(target - curr)]
            lst.add(curr)
        return -1