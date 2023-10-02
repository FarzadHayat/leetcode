# https://leetcode.com/problems/sliding-window-maximum


# O(n*k) time, O(n) space
# Brute force solution
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        res = []
        n = len(nums)
        for i in range(n - k + 1):
            j = i + k - 1
            window = []
            for x in range(i, j + 1):
                window.append(nums[x])
            res.append(max(window))
        return res


from collections import deque


# O(nlogn) time, O(n) space
# Sliding window solution using deque
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        res = []
        n = len(nums)
        # monotonically decreasing queue
        q = deque()
        # starting window
        for i in range(k):
            while q and q[-1] < nums[i]:
                q.pop()
            q.append(nums[i])
        res.append(q[0])
        for l in range(n - k):
            r = l + k
            # update left side
            if q[0] == nums[l]:
                q.popleft()
            # update right side
            while q and q[-1] < nums[r]:
                q.pop()
            q.append(nums[r])
            # add largest in current window
            res.append(q[0])
        return res


print(
    Solution().maxSlidingWindow(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3)
    == [3, 3, 5, 5, 6, 7]
)
print(Solution().maxSlidingWindow(nums=[1, 2, 3], k=1) == [1, 2, 3])
print(Solution().maxSlidingWindow(nums=[-5, -1, -2, -3], k=3) == [-1, -1])
print(Solution().maxSlidingWindow(nums=[1, 2, 3], k=2) == [2, 3])
print(Solution().maxSlidingWindow(nums=[1, 2, 3], k=3) == [3])
print(Solution().maxSlidingWindow(nums=[1], k=1) == [1])
print(
    Solution().maxSlidingWindow(nums=list(range(10**5)), k=1) == list(range(10**5))
)
print(
    Solution().maxSlidingWindow(nums=list(reversed(range(10**5))), k=1)
    == list(reversed(range(10**5)))
)
print(Solution().maxSlidingWindow(nums=[5, 4, 3, 2, 1], k=3) == [5, 4, 3])
