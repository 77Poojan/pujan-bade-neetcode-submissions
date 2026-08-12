from collections import defaultdict
from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_string = ""

        for s in strs:
            encoded_string += str(len(s)) + "#" + s

        return encoded_string

    def decode(self, s: str) -> List[str]:
        i = 0
        decoded_strs = []
        n = len(s)

        while i < n:
            j = i
            while s[j] != "#":
                j += 1

            l = int(s[i:j])
            i = j + 1
            j = i + l

            decoded_strs.append(s[i: j])
            i = j
 

        return decoded_strs