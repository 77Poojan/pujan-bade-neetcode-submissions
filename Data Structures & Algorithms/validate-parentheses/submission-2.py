class Solution:
    def isValid(self, s: str) -> bool:
        hashMap = {
            "[": "]",
            "{": "}",
            "(": ")"
        }

        stack = []
        for ch in s:
            if stack and hashMap.get(stack[-1]) == ch:
                stack.pop()
            else:
                stack.append(ch)
        
        return False if stack else True
