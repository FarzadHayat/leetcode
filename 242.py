# O(n + m) time, O(n + m) space
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_dict = dict()
        for char in s:
            s_dict[char] = s_dict.get(char, 0) + 1
        t_dict = dict()
        for char in t:
            t_dict[char] = t_dict.get(char, 0) + 1
        return s_dict.items() == t_dict.items()