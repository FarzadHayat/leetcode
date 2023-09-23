# O(n^3) time, O(n) space
# Brute force solution (time limit exceeded on LeetCode)
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        result = []
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0 and \
                        sorted([nums[i], nums[j], nums[k]]) not in result:
                        result.append(sorted([nums[i], nums[j], nums[k]]))
        return result

# O(n^2) time, O(n) space
# Two pointers solution
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        mynum = sorted(nums)
        n = len(mynum)
        result = []

        for i in range(n):
            if mynum[i] > 0:
                break
            if i > 0 and mynum[i] == mynum[i - 1]:
                continue

            l, r = i + 1, n - 1
            while l < r:
                total = mynum[i] + mynum[l] + mynum[r]
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    result.append([mynum[i], mynum[l], mynum[r]])
                    l += 1
                    r -= 1
                    while mynum[l] == mynum[l - 1] and l < r:
                        l += 1
                    while mynum[r] == mynum[r + 1] and l < r:
                        r -= 1
            
        return result


print(Solution().threeSum([-1,0,1,2,-1,-4]))
print(Solution().threeSum([0,1,1]))
print(Solution().threeSum([0,0,0]))
