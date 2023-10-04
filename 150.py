# https://leetcode.com/problems/evaluate-reverse-polish-notation

import math


# O(n) time, O(n) space
# using if else chain
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        operators = {"+", "-", "*", "/"}
        stack = []
        for token in tokens:
            if token in operators:
                secondOperand = stack.pop()
                firstOperand = stack.pop()
                if token == "+":
                    stack.append(firstOperand + secondOperand)
                elif token == "-":
                    stack.append(firstOperand - secondOperand)
                elif token == "*":
                    stack.append(firstOperand * secondOperand)
                else:
                    ans = firstOperand / secondOperand
                    if ans >= 0:
                        stack.append(math.floor(ans))
                    else:
                        stack.append(math.ceil(ans))
            else:
                stack.append(int(token))
        return stack.pop()


# O(n) time, O(n) space
# using switch statement
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        operators = {"+", "-", "*", "/"}
        stack = []
        for token in tokens:
            if token in operators:
                secondOperand = stack.pop()
                firstOperand = stack.pop()
                match token:
                    case "+":
                        stack.append(firstOperand + secondOperand)
                    case "-":
                        stack.append(firstOperand - secondOperand)
                    case "*":
                        stack.append(firstOperand * secondOperand)
                    case "/":
                        ans = firstOperand / secondOperand
                        if ans >= 0:
                            stack.append(math.floor(ans))
                        else:
                            stack.append(math.ceil(ans))
            else:
                stack.append(int(token))
        return stack.pop()


# O(n) time, O(n) space
# using operator to function map
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        operations = {
            "+": int.__add__,
            "-": int.__sub__,
            "*": int.__mul__,
            "/": lambda a, b: a // b if (a / b) >= 0 else math.ceil(a / b),
        }
        stack = []
        for token in tokens:
            if token in operations.keys():
                second = stack.pop()
                first = stack.pop()
                stack.append(operations[token](first, second))
            else:
                stack.append(int(token))
        return stack.pop()


print(Solution().evalRPN(["2", "1", "+", "3", "*"]) == 9)
print(Solution().evalRPN(["4", "13", "5", "/", "+"]) == 6)
print(
    Solution().evalRPN(
        ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    )
    == 22
)
