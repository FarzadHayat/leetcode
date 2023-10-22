from math import ceil
from typing import List


class Solution:
    def minGroupsForValidAssignment(self, nums: List[int]) -> int:
        # get freq dict of nums
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        # find max size for a group
        max_size = min(freq.values()) + 1
        # count groups needed
        groups_needed = 0
        for group in freq.values():
            groups_needed += ceil(group / max_size)
        return groups_needed


print(Solution().minGroupsForValidAssignment([3, 2, 3, 2, 3]) == 2)
print(Solution().minGroupsForValidAssignment([10, 10, 10, 3, 1, 1]) == 4)
print(Solution().minGroupsForValidAssignment([1, 1, 3, 3, 1, 1, 2, 2, 3, 1, 3, 2]) == 5)

# UNSOLVED
# problem is that splitting the nums of a certain value into groups may create groups that
# are more than one size smaller than max_size e.g. say max size = 4 and we have 5 3s, then
# the algorithm would split it into a group of 4 and a group of 1, but 1 is more than one
# size smaller than 4. So we need to find a way to split the groups so that the difference
# between the largest and smallest group is at most 1.
