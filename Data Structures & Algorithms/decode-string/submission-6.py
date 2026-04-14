class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for ch in s:
            if ch == "]":
                # get substring
                curr = []
                while stack[-1] != "[":
                    curr.append(stack.pop())
                stack.pop()  # remove "["

                # get number
                num = []
                while stack and stack[-1].isdigit():
                    num.append(stack.pop())
                k = int("".join(reversed(num)))

                # repeat and push back
                decoded = "".join(reversed(curr)) * k
                stack.append(decoded)

            else:
                stack.append(ch)

        return "".join(stack)
