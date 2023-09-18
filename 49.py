import collections

# O(nm) time, O(nm) space
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups = collections.defaultdict(list)

        for myStr in strs:
            count = [0] * 26
            for char in myStr:
                count[ord(char) - ord('a')] += 1
            groups[tuple(count)].append(myStr)
        
        return groups.values()