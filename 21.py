# https://leetcode.com/problems/merge-two-sorted-lists

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
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        head = ListNode(0, None)
        curr = head
        l1 = list1
        l2 = list2
        while True:
            # stop if either list is empty and join the rest of the other list
            if l1 is None:
                curr.next = l2
                break
            elif l2 is None:
                curr.next = l1
                break

            # add smaller of the two heads to the list and update head for that list
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next

            # update tail
            curr = curr.next

        # skip dummy node
        return head.next


# O(n) time, O(1) space
# Recursive solution
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        elif list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2


# O(n) time, O(1) space
# Tail recursive solution
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        elif list1.val < list2.val:
            return ListNode(list1.val, self.mergeTwoLists(list1.next, list2))
        else:
            return ListNode(list2.val, self.mergeTwoLists(list1, list2.next))


print(
    Solution().mergeTwoLists(
        list1=ListNode(1, ListNode(2, ListNode(4))),
        list2=ListNode(1, ListNode(3, ListNode(4))),
    )
    == ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(4))))))
)

print(
    Solution().mergeTwoLists(
        None,
        None,
    )
    == None
)

print(
    Solution().mergeTwoLists(
        None,
        ListNode(0, None),
    )
    == ListNode(0, None)
)

print(
    Solution().mergeTwoLists(
        ListNode(0, None),
        None,
    )
    == ListNode(0, None)
)
