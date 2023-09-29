# https://leetcode.com/problems/permutation-in-string

import collections


# O(n) time, O(1) space
# My solution using hash map
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # edge case
        if s1 == "":
            return True
        # freq dict of s1
        d1 = collections.defaultdict(int)  # at most 26 entries
        for char in s1:
            d1[char] += 1
        # sliding window on s2
        n = len(s2)
        d2 = collections.defaultdict(int)  # at most 26 entries
        count = 0
        l = 0
        for r in range(n):
            # increment window r
            d2[s2[r]] += 1
            count += 1
            # move window l forward until size matches s1
            while count > len(s1):
                d2[s2[l]] -= 1
                count -= 1
                if d2[s2[l]] == 0:
                    del d2[s2[l]]
                l += 1
            # check if chars in window match chars in s1
            if d1 == d2:
                return True
        # permutation of s1 not found in s2
        return False


# O(n) time, O(1) space
# My solution using arrays
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # edge case
        if s1 == "":
            return True
        # freq dict of s1
        d1 = [0] * 26
        for char in s1:
            d1[ord(char) - ord("a")] += 1
        # sliding window on s2
        n = len(s2)
        d2 = [0] * 26
        l = 0
        for r in range(n):
            # increment window r
            d2[ord(s2[r]) - ord("a")] += 1
            # move window l forward to match s1
            if r >= len(s1):
                d2[ord(s2[l]) - ord("a")] -= 1
                l += 1
            # check if chars in window match chars in s1
            if d1 == d2:
                return True
        # permutation of s1 not found in s2
        return False


# O(n) time, O(1) space
# My more optimised solution using arrays with hint from NeetCode
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # edge case
        if s1 == "":
            return True
        # freq dict of s1
        d1 = [0] * 26
        for char in s1:
            d1[ord(char) - ord("a")] += 1
        # sliding window on s2
        n = len(s2)
        d2 = [0] * 26
        l = 0
        # keep track of number of characters that have a matching frequency
        matches = 0
        for i in range(26):
            if d1[i] == d2[i]:
                matches += 1
        for r in range(n):
            # increment window r
            idx = ord(s2[r]) - ord("a")
            matched = d1[idx] == d2[idx]
            if d1[idx] == d2[idx]:
                matches -= 1
            elif d1[idx] == d2[idx] + 1:
                matches += 1
            d2[idx] += 1
            # move window l forward to match s1
            if r >= len(s1):
                idx = ord(s2[l]) - ord("a")
                if d1[idx] == d2[idx]:
                    matches -= 1
                elif d1[idx] == d2[idx] - 1:
                    matches += 1
                d2[idx] -= 1
                l += 1
            # check if chars in window match chars in s1
            if matches == 26:
                return True
        # permutation of s1 not found in s2
        return False


print(Solution().checkInclusion(s1="", s2="") == True)
print(Solution().checkInclusion(s1="", s2="a") == True)
print(Solution().checkInclusion(s1="a", s2="") == False)
print(Solution().checkInclusion(s1="a", s2="a") == True)
print(Solution().checkInclusion(s1="a", s2="aa") == True)
print(Solution().checkInclusion(s1="a", s2="ab") == True)
print(Solution().checkInclusion(s1="a", s2="b") == False)
print(Solution().checkInclusion(s1="ab", s2="eidbaooo") == True)
print(Solution().checkInclusion(s1="ab", s2="eidboaoo") == False)
print(Solution().checkInclusion(s1="obd", s2="eidboaoo") == True)
print(Solution().checkInclusion(s1="obo", s2="eidboaoo") == False)
print(Solution().checkInclusion(s1="abc", s2="bbbca") == True)
