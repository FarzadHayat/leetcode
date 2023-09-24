# O(n) time, O(1) space
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count = [0,0]
        for n in s:
            count[int(n)] += 1
        return "1" * (count[1] - 1) + "0" * count[0] + "1"