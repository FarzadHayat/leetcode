# https://leetcode.com/problems/daily-temperatures


# O(n^2) time, O(n) space
# Brute force solution
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        res = []

        for i, temp in enumerate(temperatures):
            days = 0
            for j in range(i + 1, len(temperatures)):
                if temp < temperatures[j]:
                    days = j - i
                    break
            res.append(days)

        return res


# O(n) time, O(n) space
# Monotonic non-increasing stack solution
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        output = [0] * len(temperatures)
        stack = []  # indices of values in temp

        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                idx = stack.pop()
                output[idx] = i - idx  # num days it took to get a higher temp
            stack.append(i)

        return output


print(
    Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])
    == [1, 1, 4, 2, 1, 1, 0, 0]
)
print(Solution().dailyTemperatures([30, 40, 50, 60]) == [1, 1, 1, 0])
print(Solution().dailyTemperatures([30, 60, 90]) == [1, 1, 0])
print(Solution().dailyTemperatures([0, 3, 1, 2, 4]) == [1, 3, 1, 1, 0])
print(Solution().dailyTemperatures([0, 3, 2, 1, 4]) == [1, 3, 2, 1, 0])
