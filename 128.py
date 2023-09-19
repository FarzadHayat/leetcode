# O(n) time, O(n) space
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
        
        numset = set(nums)
        longest = 0

        for num in numset:
            if (num - 1) not in numset:
                rsf = 1
                while num + rsf in numset:
                    rsf += 1
                longest = max(longest, rsf)
        
        return longest

print(Solution().longestConsecutive([100,4,200,1,3,2])) # == 4)
print(Solution().longestConsecutive([0,3,7,2,5,8,4,6,0,1])) # == 9)
print(Solution().longestConsecutive([4,0,-4,-2,2,5,2,0,-8,-8,-8,-8,-1,7,4,5,5,-4,6,6,-3])) # == 5