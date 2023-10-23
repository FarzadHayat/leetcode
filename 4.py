# https://leetcode.com/problems/median-of-two-sorted-arrays

from typing import List


# O(log (m + n)) time, O(1) space
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2
        # make sure A is the shorter array
        if len(A) > len(B):
            A, B = B, A
        # left and right pointers for A
        l, r = 0, len(A) - 1
        while True:
            # left partition A includes i
            i = l + (r - l) // 2
            # left partition of B includes j
            j = half - i - 2
            # last element in left partition of A
            Aleft = A[i] if i >= 0 else float("-inf")
            # first element in right partition of A
            Aright = A[i + 1] if i + 1 < len(A) else float("inf")
            # last element in left partition of B
            Bleft = B[j] if j >= 0 else float("-inf")
            # first element in right partition of B
            Bright = B[j + 1] if j + 1 < len(B) else float("inf")
            # A is partitioned too much to the right
            if Aleft > Bright:
                r = i - 1
            # A is partitioned too much to the left
            elif Bleft > Aright:
                l = i + 1
            # the partitioning is correct
            else:
                # find the median
                if total % 2 == 0:
                    median = (max(Aleft, Bleft) + min(Aright, Bright)) / 2
                else:
                    median = min(Aright, Bright)
                return median


print(Solution().findMedianSortedArrays(nums1=[1], nums2=[2]) == 1.5)

print(Solution().findMedianSortedArrays(nums1=[1], nums2=[2, 3]) == 2)
print(Solution().findMedianSortedArrays(nums1=[1, 3], nums2=[2]) == 2)

print(Solution().findMedianSortedArrays(nums1=[1, 2], nums2=[3, 4]) == 2.5)

print(
    Solution().findMedianSortedArrays(
        nums1=[1, 2, 3, 4, 5], nums2=[1, 2, 3, 4, 5, 6, 7]
    )
    == 3.5
)

print(
    Solution().findMedianSortedArrays(
        nums1=[1, 2, 3, 4, 5], nums2=[1, 2, 3, 4, 5, 6, 7, 8]
    )
    == 4
)

print(
    Solution().findMedianSortedArrays(
        nums1=[1, 1, 1, 2, 5], nums2=[1, 1, 2, 2, 3, 4, 8]
    )
    == 2
)

print(
    Solution().findMedianSortedArrays(
        nums1=[1, 1, 1, 2, 5], nums2=[1, 1, 3, 3, 3, 4, 8, 9]
    )
    == 3
)

print(
    Solution().findMedianSortedArrays(
        nums1=[1, 5, 10, 100, 200], nums2=[3, 3, 4, 6, 7, 8, 8]
    )
    == 6.5
)

print(Solution().findMedianSortedArrays(nums1=[1, 2, 4], nums2=[100, 200, 300]) == 52)
