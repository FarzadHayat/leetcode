# https://leetcode.com/problems/remove-nth-node-from-end-of-list

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
# Iterate through list once to find length, then a second time to find the node and remove it.
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # get size of list
        size = 0
        curr = head
        while curr:
            curr = curr.next
            size += 1

        # index of node to be removed
        to_remove = size - n
        # iterate until you find node at index i
        i = 0
        prev = None
        curr = head
        next = curr.next
        while i < to_remove:
            prev = curr
            curr = next
            next = curr.next
            i += 1
        # remove the node from the list
        if not prev:
            head = next
        else:
            prev.next = next
        return head


# O(n) time, O(1) space
# Use two pointers with a gap of n between them.
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # create dummy pointer before head and use it for the left pointer
        dummy = ListNode(0, head)
        left = dummy
        right = head
        # move right pointer forward n nodes
        while n > 0 and right:
            right = right.next
            n -= 1
        # move both pointers at the same rate until right is at the end of the list
        while right:
            left = left.next
            right = right.next
        # left pointer is now pointing at the node before the one we want to remove
        # delete node
        left.next = left.next.next
        return dummy.next


print(
    Solution().removeNthFromEnd(
        ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None))))), 2
    )
    == ListNode(1, ListNode(2, ListNode(3, ListNode(5, None))))
)

print(
    Solution().removeNthFromEnd(
        ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None))))), 1
    )
    == ListNode(1, ListNode(2, ListNode(3, ListNode(4, None))))
)

print(
    Solution().removeNthFromEnd(
        ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None))))), 5
    )
    == ListNode(2, ListNode(3, ListNode(4, ListNode(5, None))))
)

print(Solution().removeNthFromEnd(ListNode(1, None), 1) == None)

print(
    Solution().removeNthFromEnd(ListNode(1, ListNode(2, None)), 1) == ListNode(1, None)
)

print(
    Solution().removeNthFromEnd(ListNode(1, ListNode(2, None)), 2) == ListNode(2, None)
)
