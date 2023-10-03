# https://leetcode.com/problems/min-stack


# O(1) time for all operations, O(n) space for the stack
# My solution - use a second list to keep track of the min
# in stack up to and including that index
class MinStack:
    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min:
            self.min.append(min(self.min[-1], val))
        else:
            self.min.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())
# return -3
minStack.pop()
print(minStack.top())
# return 0
print(minStack.getMin())
# return -2
