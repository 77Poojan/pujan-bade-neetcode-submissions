class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def is_palindrome(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
    

        def backtrack(i, sol):
            if i == len(s): 
                res.append(sol[:])
                return

            for j in range(i, len(s)):
                if is_palindrome(i, j):
                    sol.append(s[i : j+1])
                    backtrack(j + 1, sol)
                    sol.pop()

        backtrack(0, [])
        return res
        
