class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch == "]":
                arr = []
                while stack and stack[-1] != "[":
                    item = stack.pop()
                    arr.append(item)
                
                stack.pop()   
                counter = ""
                while stack and stack[-1].isdigit():
                    counter += stack.pop() 
                    
                counter = counter[::-1]

                counter = int(counter)
                arr = arr[::-1]
                strs = "".join(arr)
                new_s = ""
                
                while counter > 0:
                    new_s += strs
                    counter -= 1
                    
                stack.append(new_s)
   
            else:
                stack.append(ch)
                
        return "".join(stack)

            