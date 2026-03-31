class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1

        while i <= j:
            x = s[i].isalnum() 
            y = s[j].isalnum()
            if x and y and s[i].lower() != s[j].lower():  
                return False
            if x and not y:
                j -= 1
            elif not x and y:
                i += 1
            else:
                i += 1
                j -= 1
        return True