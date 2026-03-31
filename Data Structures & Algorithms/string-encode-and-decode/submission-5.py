class Solution:
    def encode(self, strs: List[str]) -> str:
        new_str = ""
        for s in strs:
            new_str = new_str + str(len(s)) + "#" + s
        return new_str

    def decode(self, s: str) -> List[str]:
        i = 0
        l = []

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            i = j + 1
            j = i + length
            l.append(s[i: j])
            i = j

        return l
        
            