# https://leetcode.com/problems/generate-parentheses


# O(2^n) time, O(2^n) space
# Recursive solution
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        if n == 1:
            return ["()"]
        else:
            prev = self.generateParenthesis(n - 1)
            res = set()
            l, r = n - 1, 2 * n - 1
            for par in prev:
                for i in range(l, r):
                    new = par[:i] + "()" + par[i:]
                    res.add(new)
            return sorted(list(res))


# O(2^n) time, O(2^n) space
# NeetCode's stack solution
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        stack = []
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0, 0)
        return res


print(Solution().generateParenthesis(1) == ["()"])
print(Solution().generateParenthesis(2) == ["(())", "()()"])
print(
    Solution().generateParenthesis(3)
    == ["((()))", "(()())", "(())()", "()(())", "()()()"]
)
print(
    Solution().generateParenthesis(4)
    == [
        "(((())))",
        "((()()))",
        "((())())",
        "((()))()",
        "(()(()))",
        "(()()())",
        "(()())()",
        "(())(())",
        "(())()()",
        "()((()))",
        "()(()())",
        "()(())()",
        "()()(())",
        "()()()()",
    ]
)
