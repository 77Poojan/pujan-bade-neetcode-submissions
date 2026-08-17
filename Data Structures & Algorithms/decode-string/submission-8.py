class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for ch in s:
            if ch == "]":
                w = []
                
                while stack[-1] != "[":
                    w.append(stack.pop())
                
                stack.pop()
                num = []
                while stack and stack[-1].isdigit():
                    num.append(stack.pop())

                num = int("".join(reversed(num)))
                decoded = "".join(reversed(w)) * num
                stack.append(decoded)

            else:
                stack.append(ch)

        return "".join(stack)
