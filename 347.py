# O(nlogn) time, O(n) space
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freqs = dict()
        for num in nums:
            freqs[num] = freqs.get(num, 0) + 1
        return map(lambda x: x[0], sorted(freqs.items(), key=lambda x: x[1], reverse=True))[:k]

# O(n) time, O(n) space
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # get frequencies
        freq = dict()
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        # bucket sort into count list
        count = [[] for i in range(len(nums) + 1)]
        for key, val in freq.items():
            count[val].append(key)
        
        # get the most frequent by working back from the end of the list
        result = []
        for i in range(len(nums), 0, -1):
            if len(result) >= k:
                break
            to_add = min(k - len(result), len(count[i]))
            result += count[i][:to_add]
        return result

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

print(Solution().topKFrequent([1,1,1,2,2,3], 2))

