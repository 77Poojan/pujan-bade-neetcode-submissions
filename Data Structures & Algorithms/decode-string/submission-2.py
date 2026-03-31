class Solution:
    def decodeString(self, s: str) -> str:
        # stack = []
        # for ch in s:
        #     if ch == "]":
        #         ec = ""
        #         while stack and stack[-1] != "[":
        #             ec += stack.pop() 
                    
        #         stack.pop()
        #         cc = ""
        #         while stack and stack[-1].isdigit():
        #             cc += stack.pop()

        #         n = int(cc[::-1])
        #         while  n > 0:   
        #             stack.extend(ec[::-1])
        #             n -= 1
        #     else:
        #         stack.append(ch)
        # return "".join(stack)


        stack = []

        for ch in s:
            if ch != "]":
                stack.append(ch)
            else:
                # collect encoded string
                curr = []
                while stack[-1] != "[":
                    curr.append(stack.pop())
                stack.pop()  # remove '['

                # collect number
                num = []
                while stack and stack[-1].isdigit():
                    num.append(stack.pop())

                repeat = int("".join(reversed(num)))
                decoded = curr[::-1] * repeat

                stack.extend(decoded)

        return "".join(stack)
