# https://leetcode.com/problems/reverse-linked-list

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
# Iterative solution
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # empty list edge case
        if head is None:
            return
        # setup pointers
        prev = None
        curr = head
        next = head.next

        # loop through list and reverse direction of next pointers
        while next:
            curr.next = prev
            prev = curr
            curr = next
            next = curr.next
        # adjustment for last pointer
        curr.next = prev
        # return new head
        return curr


# O(n) time, O(1) space
# Recursive solution
class Solution:
    def reverseList(
        self, head: Optional[ListNode], prev: Optional[ListNode] = None
    ) -> Optional[ListNode]:
        # empty list edge case
        if head is None:
            return prev
        else:
            next = head.next
            head.next = prev
            prev = head
            return self.reverseList(next, prev)


# O(n) time, O(1) space
# Slightly less readable tail recursive version
class Solution:
    def reverseList(
        self, head: Optional[ListNode], prev: Optional[ListNode] = None
    ) -> Optional[ListNode]:
        return (
            prev
            if head is None
            else self.reverseList(head.next, ListNode(head.val, prev))
        )


print(
    Solution().reverseList(
        ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
    )
    == ListNode(5, ListNode(4, ListNode(3, ListNode(2, ListNode(1, None)))))
)

print(
    Solution().reverseList(ListNode(1, ListNode(2, None)))
    == ListNode(2, ListNode(1, None))
)

print(Solution().reverseList(ListNode(1, None)) == ListNode(1, None))
print(Solution().reverseList(None) == None)
