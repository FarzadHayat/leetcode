# O(n) time, O(1) space
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l, r = 0, len(numbers) - 1
        sum = numbers[l] + numbers[r]
        while sum != target:
            if sum < target:
                l += 1
            else:
                r -= 1
            sum = numbers[l] + numbers[r]
        return [l + 1, r + 1]

print(Solution().twoSum(numbers = [2,7,11,15], target = 9)) # [1,2]
print(Solution().twoSum(numbers = [2,3,4], target = 6)) # [1,3]
print(Solution().twoSum(numbers = [-1,0], target = -1)) # [1,2]