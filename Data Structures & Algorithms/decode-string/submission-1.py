class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch == "]":
                ec = ""
                while stack and stack[-1] != "[":
                    ec += stack.pop() 
                    
                stack.pop()
                cc = ""
                while stack and stack[-1].isdigit():
                    cc += stack.pop()
                n = int(cc[::-1])
                while  n > 0:   
                    stack.extend(ec[::-1])
                    n -= 1
            else:
                stack.append(ch)
        return "".join(stack)