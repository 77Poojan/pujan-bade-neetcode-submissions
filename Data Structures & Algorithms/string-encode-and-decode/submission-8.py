class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s 
        return res
        

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            digit = ""
            while s[i].isdigit():
                digit += s[i]
                i += 1
                
            j = int(digit)
            i += 1
            word = s[i: i + j]
            res.append(word)
            i += len(word)
           
        return res 
            