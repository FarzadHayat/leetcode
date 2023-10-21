# https://leetcode.com/problems/time-based-key-value-store

from collections import defaultdict


# get uses binary search to find value for largest time that is not greater than the timestamp
class TimeMap:
    # O(1) time, O(1) space
    def __init__(self):
        self.time_map = defaultdict(list)

    # O(1) time, O(1) space
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((value, timestamp))

    # O(log n) time, O(1) space
    def get(self, key: str, timestamp: int) -> str:
        value_time = self.time_map[key]
        l, r = 0, len(value_time) - 1
        best = ""
        while l <= r:
            m = l + (r - l) // 2
            val, time = value_time[m]
            # found timestamp
            if time == timestamp:
                best = val
                break
            # timestamp is in right half
            elif time < timestamp:
                l = m + 1
                best = val
            # timestamp is in left half
            else:
                r = m - 1
        return best


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

timeMap = TimeMap()
timeMap.set("foo", "bar", 1)
print(timeMap.get("foo", 1) == "bar")
print(timeMap.get("foo", 3) == "bar")
timeMap.set("foo", "bar2", 4)
print(timeMap.get("foo", 4) == "bar2")
print(timeMap.get("foo", 5) == "bar2")
