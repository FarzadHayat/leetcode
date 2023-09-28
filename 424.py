# https://leetcode.com/problems/longest-repeating-character-replacement


# O(n) time, O(1) space
# My solution with hints from NeetCode's video
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        count = dict()
        max_freq = 0
        longest = 0
        l = 0

        for r in range(n):
            # add new char to window on the right
            count[s[r]] = 1 + count.get(s[r], 0)
            max_freq = max(max_freq, count[s[r]])
            # shrink window from left if necessary to make it valid
            while (r - l + 1 - max_freq) > k:
                count[s[l]] -= 1
                l += 1
            # calculate new longest substring
            longest = max(longest, r - l + 1)

        return longest


print(Solution().characterReplacement(s="A", k=0) == 1)
print(Solution().characterReplacement(s="A", k=1) == 1)
print(Solution().characterReplacement(s="AA", k=0) == 2)
print(Solution().characterReplacement(s="AB", k=0) == 1)
print(Solution().characterReplacement(s="AB", k=1) == 2)
print(Solution().characterReplacement(s="AB", k=2) == 2)
print(Solution().characterReplacement(s="ABC", k=0) == 1)
print(Solution().characterReplacement(s="ABC", k=1) == 2)
print(Solution().characterReplacement(s="ABC", k=2) == 3)
print(Solution().characterReplacement(s="ABAB", k=0) == 1)
print(Solution().characterReplacement(s="ABAB", k=1) == 3)
print(Solution().characterReplacement(s="ABAB", k=2) == 4)
print(Solution().characterReplacement(s="AABABBA", k=1) == 4)
print(Solution().characterReplacement(s="AABABBB", k=1) == 5)
print(Solution().characterReplacement(s="AABAABB", k=1) == 5)
print(Solution().characterReplacement(s="ABBBABBA", k=3) == 8)
print(Solution().characterReplacement(s="AAABCD", k=1) == 4)
