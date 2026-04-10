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
                
            dec, j = "", 0
            while j < int(digit):
                i += 1
                dec += s[i]
                j += 1

            res.append(dec)
            i += 1
        return res 
            