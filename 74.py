# https://leetcode.com/problems/search-a-2d-matrix


# O(m + log(n)) time, O(n) space
# m for finding the correct row, log(n) for finding the element in that row if it exists
# m is num rows
# n is num columns
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        for row in matrix:
            if target <= row[-1]:
                return self.binarySearch(row, target)
        return False

    def binarySearch(self, nums: list[int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if target < nums[m]:
                r = m - 1
            elif target > nums[m]:
                l = m + 1
            else:
                return True
        return False


# O(log(m * n)) time, O(n) space
# Time complexity is log(m) + log(n) which equals log(m * n)
# m is num rows
# n is num columns
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        while l < r:
            m = l + (r - l) // 2
            if target < matrix[m][-1]:
                r = m
            elif target > matrix[m][-1]:
                l = m + 1
            else:
                return True
        if l == r:
            return self.binarySearch(matrix[l], target)
        return False

    def binarySearch(self, nums: list[int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if target < nums[m]:
                r = m - 1
            elif target > nums[m]:
                l = m + 1
            else:
                return True
        return False


print(
    Solution().searchMatrix(
        matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=3
    )
    == True
)
print(
    Solution().searchMatrix(
        matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=10
    )
    == True
)
print(
    Solution().searchMatrix(
        matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=20
    )
    == True
)
print(
    Solution().searchMatrix(
        matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=0
    )
    == False
)
print(
    Solution().searchMatrix(
        matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=13
    )
    == False
)
print(
    Solution().searchMatrix(
        matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=100
    )
    == False
)
