class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op not in ["C", "D", "+"]:
                stack.append(int(op))
            elif op == "+":
                stack.append(int(stack[-1]) + int(stack[-2]))
            elif op == "C" and stack:
                stack.pop()
            elif op == "D" and stack:
                stack.append(int(stack[-1]) * 2)
        return sum(stack)