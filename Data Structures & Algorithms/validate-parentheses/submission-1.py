class Solution:
    def isValid(self, s: str) -> bool:
        sets = {
            "(": ")",
            "{": "}",
            "[": "]"
        }
        stack = [s[0]]
        i = 1

        while i < len(s):
            if len(stack) == 0:
                stack.append(s[i])
                i += 1
                continue
            
            k = stack[-1]
            if k in sets.keys() and sets[k] == s[i]:
                stack.pop()
            else:
                stack.append(s[i])
            i += 1
            
        if len(stack) == 0:
            return True
        else:
            return False