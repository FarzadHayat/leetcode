# https://leetcode.com/problems/koko-eating-bananas

from math import ceil


# O(n * m) time, O(1) space
# where m is the max value in piles
# Brute force solution
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        def numHours(k: int) -> int:
            n = 0
            for pile in piles:
                n += ceil(pile / k)
            return n

        for i in range(1, max(piles) + 1):
            if numHours(i) <= h:
                return i
        return -1


# O(log(m) * n) time, O(1) space
# where m is the max value in piles
# Binary search solution
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        def numHours(k: int) -> int:
            """Return num hours to eat all files given k
            O(n) time, O(1) space"""
            n = 0
            for pile in piles:
                n += ceil(pile / k)
            return n

        l, r = 1, max(piles)
        best = r
        while l <= r:
            m = l + (r - l) // 2
            hours = numHours(m)
            if hours <= h:
                best = min(best, m)
                r = m - 1
            elif hours > h:
                l = m + 1
        return best


print(Solution().minEatingSpeed(piles=[3, 6, 7, 11], h=8) == 4)
print(Solution().minEatingSpeed(piles=[30, 11, 23, 4, 20], h=5) == 30)
print(Solution().minEatingSpeed(piles=[30, 11, 23, 4, 20], h=6) == 23)
print(Solution().minEatingSpeed(piles=[312884470], h=312884469) == 2)
