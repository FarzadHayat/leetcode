# https://leetcode.com/problems/reorder-list

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"ListNode({self.val}, {repr(self.next)})"

    def __eq__(self, other):
        return self.val == other.val and self.next == other.next


# O(n) time, O(1) space
# Split into two halves, reverse second half, zip merge two halves
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head
        # find second half of list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None

        # reverse second half
        prev = None
        next = second.next
        while next:
            second.next = prev
            prev = second
            second = next
            next = second.next
        second.next = prev

        # merge the two halves into new list
        left, right = head, second
        while right:
            nextL, nextR = left.next, right.next
            left.next, right.next = right, nextL
            left, right = nextL, nextR
        return head


print(Solution().reorderList(None) == None)


print(Solution().reorderList(ListNode(1, None)) == ListNode(1, None))


print(
    Solution().reorderList(ListNode(1, ListNode(2, None)))
    == ListNode(1, ListNode(2, None))
)


print(
    Solution().reorderList(ListNode(1, ListNode(2, ListNode(3, None))))
    == ListNode(1, ListNode(3, ListNode(2, None)))
)


print(
    Solution().reorderList(ListNode(1, ListNode(2, ListNode(3, ListNode(4, None)))))
    == ListNode(1, ListNode(4, ListNode(2, ListNode(3, None))))
)


print(
    Solution().reorderList(
        ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
    )
    == ListNode(1, ListNode(5, ListNode(2, ListNode(4, ListNode(3, None)))))
)
