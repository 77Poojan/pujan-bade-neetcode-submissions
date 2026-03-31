class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for ch in s:
            if ch != "]":
                stack.append(ch)
            else:
                curr = []
                while stack and stack[-1] !="[":
                    curr.append(stack.pop())
                stack.pop()
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(int(k) * "".join(curr[::-1]))

        return "".join(stack)