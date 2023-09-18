# O(n) time, O(n) space
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        ltr = []
        prod = 1
        for num in nums:
            prod *= num
            ltr.append(prod)

        rtl = []
        prod = 1
        for num in nums[::-1]:
            prod *= num
            rtl.append(prod)
        rtl.reverse()    

        res = []
        res.append(rtl[1])
        for i in range(1, len(nums) - 1):
            res.append(ltr[i - 1] * rtl[i + 1])
        res.append(ltr[-2])

        return res

# O(n) time, O(n) space
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

print(Solution().productExceptSelf([1,2,3,4]))