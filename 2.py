# https://leetcode.com/problems/add-two-numbers

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"ListNode({self.val}, {repr(self.next)})"

    def __eq__(self, other):
        return id(self) == id(other) or (
            self and other and self.val == other.val and self.next == other.next
        )


# O(n) time, O(1) space
# where n is the length of the longer list
# Iterate through both lists simultaneously, adding the values and keeping track of the carry.
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        h1 = l1
        h2 = l2
        curr = ListNode()
        head = curr
        carry = 0
        while h1 or h2 or carry:
            val = carry
            if h1:
                val += h1.val
                h1 = h1.next
            if h2:
                val += h2.val
                h2 = h2.next
            rem = val % 10
            carry = val // 10
            curr.next = ListNode(rem)
            curr = curr.next
        return head.next


# NeetCode's solution
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        cur = dummy

        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # new digit
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)

            # update ptrs
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next


# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
l1 = ListNode(2, ListNode(4, ListNode(3, None)))
l2 = ListNode(5, ListNode(6, ListNode(4, None)))
print(Solution().addTwoNumbers(l1, l2) == ListNode(7, ListNode(0, ListNode(8, None))))

# Input: l1 = [0], l2 = [0]
# Output: [0]
l1 = ListNode(0, None)
l2 = ListNode(0, None)
print(Solution().addTwoNumbers(l1, l2) == ListNode(0, None))

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
l1 = ListNode(
    9,
    ListNode(
        9,
        ListNode(
            9,
            ListNode(
                9,
                ListNode(
                    9,
                    ListNode(
                        9,
                        ListNode(
                            9,
                            None,
                        ),
                    ),
                ),
            ),
        ),
    ),
)
l2 = ListNode(
    9,
    ListNode(
        9,
        ListNode(
            9,
            ListNode(
                9,
                None,
            ),
        ),
    ),
)
print(
    Solution().addTwoNumbers(l1, l2)
    == ListNode(
        8,
        ListNode(
            9,
            ListNode(
                9,
                ListNode(
                    9,
                    ListNode(
                        0,
                        ListNode(
                            0,
                            ListNode(
                                0,
                                ListNode(
                                    1,
                                    None,
                                ),
                            ),
                        ),
                    ),
                ),
            ),
        ),
    )
)
