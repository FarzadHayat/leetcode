# https://leetcode.com/problems/minimum-window-substring


# O(n) time, O(1) space
# My solution
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        # freq dict of t string
        tCount = dict()
        for char in t:
            tCount[char] = tCount.get(char, 0) + 1
        need = len(tCount.keys())
        # sliding window
        n = len(s)
        sCount = dict()
        l = 0
        res = (-1, -1)
        size = float("inf")
        have = 0
        for r in range(n):
            # increment count of char at r if char is part of t string
            if s[r] in tCount:
                # increment by one
                sCount[s[r]] = sCount.get(s[r], 0) + 1
                if sCount[s[r]] == tCount[s[r]]:
                    have += 1
                # move l forward as much as possible while not removing essential chars
                while l < r:
                    if s[l] not in sCount:
                        l += 1
                    elif (r - l + 1) > size or sCount[s[l]] > tCount[s[l]]:
                        if sCount[s[l]] == tCount[s[l]]:
                            have -= 1
                        sCount[s[l]] -= 1
                        l += 1
                    else:
                        break
                # check if substring matches
                if have == need and (r - l + 1) < size:
                    res = (l, r)
                    size = r - l + 1
        # return valid substring if found, otherwise return empty string
        return "" if res == (-1, -1) else s[res[0] : res[1] + 1]


print(Solution().minWindow(s="ADOBECODEBANC", t="ABC") == "BANC")
print(Solution().minWindow(s="DOBECODEBANC", t="ABC") == "BANC")
print(Solution().minWindow(s="a", t="a") == "a")
print(Solution().minWindow(s="a", t="aa") == "")
print(Solution().minWindow(s="aa", t="a") == "a")
print(Solution().minWindow(s="", t="a") == "")
print(Solution().minWindow(s="abcba", t="b") == "b")
print(Solution().minWindow(s="AOBOCOABOCOABC", t="ABC") == "ABC")
print(Solution().minWindow(s="BCA", t="ABC") == "BCA")
print(Solution().minWindow(s="ABABA", t="AAA") == "ABABA")
print(Solution().minWindow(s="aaaaaaaaaaaabbbbbcdd", t="abcdd") == "abbbbbcdd")
