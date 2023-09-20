# O(n) time, O(n) space
class Solution:
    def isPalindrome(self, s: str) -> bool:
        phrase = [char for char in s.lower() if char.isalnum()]
        return phrase == phrase[::-1]
    
# O(n) time, O(1) space
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # set initial l and r pointers
        l, r = 0, len(s) - 1

        while l < r:
            # make sure l and r are pointing at alphanumeric characters
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            # check if l and r are pointing at the same char
            if s[l].lower() != s[r].lower():
                return False
            # increment l and decrement r
            l, r = l + 1, r - 1
        # no mismatches, so s is a palindrome
        return True

    def alphaNum(self, c: str) -> bool:
        return (ord('A') <= ord(c) <= ord('Z') or \
                ord('a') <= ord(c) <= ord('z') or \
                ord('0') <= ord(c) <= ord('9'))

print(Solution().isPalindrome('abcdef'))
print(Solution().isPalindrome('abcde'))

print(Solution().isPalindrome('abccba'))
print(Solution().isPalindrome('abcba'))

print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
print(Solution().isPalindrome("race a car"))
print(Solution().isPalindrome(" "))