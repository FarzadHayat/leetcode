# https://leetcode.com/problems/car-fleet


# O(n log n) time, O(n) space
# nlogn for sorting by position and O(n) time for the rest
# right to left solution
class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        position_speed = list(zip(position, speed))
        stack = []
        for p, s in sorted(position_speed):
            distance_left = target - p
            hours_left = distance_left / s
            stack.append(hours_left)
        num_fleet = 1
        prev = stack[-1]
        while stack:
            hours_left = stack.pop()
            if hours_left > prev:
                num_fleet += 1
                prev = hours_left
        return num_fleet


# O(n log n) time, O(n) space
# nlogn for sorting by position and O(n) time for the rest
# left to right solution
class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        position_speed = list(zip(position, speed))
        stack = []
        for p, s in sorted(position_speed):
            distance_left = target - p
            hours_left = distance_left / s
            while stack and stack[-1] <= hours_left:
                stack.pop()
            stack.append(hours_left)
        return len(stack)


# can we do it without sorting by position?
# can we do it using less memory?

print(Solution().carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]) == 3)
print(Solution().carFleet(10, [3], [3]) == 1)
print(Solution().carFleet(100, [0, 2, 4], [4, 2, 1]) == 1)
print(Solution().carFleet(10, [0, 1, 2, 3, 4], [1, 1, 1, 2, 3]) == 5)
print(Solution().carFleet(10, [0, 1, 2, 3, 4], [5, 4, 3, 3, 3]) == 3)
print(Solution().carFleet(10, [0, 4, 2], [2, 1, 3]) == 1)
