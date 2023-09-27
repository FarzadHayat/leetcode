# https://leetcode.com/problems/longest-substring-without-repeating-characters

# O(n^2) time, O(n) space
# My solution
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        longest = 0
        for i in range(n):
            if n - i < longest:
                break
            seen = set()
            count = 0
            j = i
            while j < n and s[j] not in seen:
                count += 1
                seen.add(s[j])
                j += 1
            longest = max(longest, count)

        return longest

# O(n) time, O(n) space
# Sliding window solution
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        seen = set()
        longest = 0
        l = 0

        for r in range(n):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            longest = max(longest, len(seen))

        return longest
    
print(Solution().lengthOfLongestSubstring("abcabcbb")) # 3
print(Solution().lengthOfLongestSubstring("bbbbb")) # 1
print(Solution().lengthOfLongestSubstring("pwwkew")) # 3
print(Solution().lengthOfLongestSubstring("abcdefghijklmnopqrstuvwxyz")) # 26
print(Solution().lengthOfLongestSubstring("aaaabcdefghijklmnopqrstuvwxyzzzz")) # 26
print(Solution().lengthOfLongestSubstring("abcabcab")) # 3
print(Solution().lengthOfLongestSubstring(" ")) # 1
print(Solution().lengthOfLongestSubstring("$ 1 % 1 $")) # 3
print(Solution().lengthOfLongestSubstring("dvdf")) # 3
print(Solution().lengthOfLongestSubstring("dvdfvabc")) # 6