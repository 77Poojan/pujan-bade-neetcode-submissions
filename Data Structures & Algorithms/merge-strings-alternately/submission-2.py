class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        word = ""
    
        if len(word1) > len(word2):
            n1 = list(word2)
            n2 = list(word1)
        else:
            n1 = list(word1)
            n2 = list(word2)
            

        while i < len(n1):
            word += word1[i] + word2[i]
            i += 1
    
        if len(n2) > i: 
            word += "".join(n2[i:])
    
        
        return word       