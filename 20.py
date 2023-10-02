# https://leetcode.com/problems/valid-parentheses


# O(n) time, O(n) space
# My solution
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char in {"(", "{", "["}:
                stack.append(char)
            elif len(stack) == 0:
                return False
            elif (
                stack[-1] == "("
                and char == ")"
                or stack[-1] == "{"
                and char == "}"
                or stack[-1] == "["
                and char == "]"
            ):
                stack.pop()
            else:
                return False

        return len(stack) == 0


# O(n) time, O(n) space
# NeetCode's solution
class Solution:
    def isValid(self, s: str) -> bool:
        map = {")": "(", "]": "[", "}": "{"}
        stack = []

        for char in s:
            if char not in map:
                stack.append(char)
                continue
            if not stack or stack[-1] != map[char]:
                return False
            stack.pop()

        return not stack


print(Solution().isValid("") == True)
print(Solution().isValid("()") == True)
print(Solution().isValid("({[()()[(){}]]})") == True)
print(Solution().isValid("()[]{}") == True)

print(Solution().isValid("(}") == False)
print(Solution().isValid("({)}") == False)
print(Solution().isValid("[{(}])") == False)
print(Solution().isValid("({[()()[{]{}]]})") == False)
print(Solution().isValid("(") == False)
print(Solution().isValid("}") == False)
print(Solution().isValid("(([])") == False)
print(Solution().isValid("([}])") == False)
