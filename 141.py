# https://leetcode.com/problems/linked-list-cycle

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"ListNode({self.val}, {repr(self.next)})"

    def __eq__(self, other):
        return id(self) == id(other)


# O(n) time, O(n) space
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        curr = head
        while curr:
            if id(curr) in seen:
                return True
            seen.add(id(curr))
            curr = curr.next
        return False


# O(n) time, O(1) space
# Floyd's tortoise and hare algorithm
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


# head = [3,2,0,-4], pos = 0
tail = ListNode(-4, None)
head = ListNode(3, ListNode(2, ListNode(0, tail)))
tail.next = head
print(Solution().hasCycle(head) == True)

# head = [3,2,0,-4], pos = 1
tail = ListNode(-4, None)
head = ListNode(3, ListNode(2, ListNode(0, tail)))
tail.next = head.next
print(Solution().hasCycle(head) == True)

# head = [3,2,0,-4], pos = 2
tail = ListNode(-4, None)
head = ListNode(3, ListNode(2, ListNode(0, tail)))
tail.next = head.next.next
print(Solution().hasCycle(head) == True)

# head = [3,2,0,-4], pos = 3
tail = ListNode(-4, None)
head = ListNode(3, ListNode(2, ListNode(0, tail)))
tail.next = tail
print(Solution().hasCycle(head) == True)

# head = [1,2], pos = 0
tail = ListNode(2, None)
head = ListNode(1, tail)
tail.next = head
print(Solution().hasCycle(head) == True)

# head = [1,2], pos = 1
tail = ListNode(2, None)
head = ListNode(1, tail)
tail.next = tail
print(Solution().hasCycle(head) == True)

# head = [1,2], pos = -1
head = ListNode(1, ListNode(2, None))
print(Solution().hasCycle(head) == False)

# head = [1], pos = 0
head = ListNode(1, None)
head.next = head
print(Solution().hasCycle(head) == True)


# head = [1], pos = -1
head = ListNode(1, None)
print(Solution().hasCycle(head) == False)
